import cv2
import os
import numpy as np
import json
import sys
from flask_restful import Resource, request
from api import settings
from keras.models import Model, load_model


class RecommendationResource(Resource):
    def get(self, user):

        artist = request.args.get("artist")
        song = request.args.get("song")

        # load model
        mod = "/home/jhonatas/development/iaa-music-discovery/scratches/multi_perceptron/saved_model/perceptron.h5"
        mod = "".join(
            [settings.BASE_DIR, "/", settings.BASE_API, "/", "cnn_model", "/", "model.h5"]
        )
        model = load_model(mod)

        matrix_size = model.layers[-2].output.shape[1]
        new_model = Model(model.inputs, model.layers[-2].output)

        SLICED_SPECS = "".join(
            [
                settings.BASE_DIR,
                "/",
                settings.BASE_API,
                "/",
                "download_pool_nexttune_sliced_spectrograms",
            ]
        )

        # images, labels = self.load_pool(settings.AUDIO_SLICED_SPECTROGRAM_FOLDER)
        images, labels = self.load_pool(SLICED_SPECS)
        print(
            SLICED_SPECS,
            file=sys.stderr,
        )
        print(
            images,
            file=sys.stderr,
        )

        images = np.expand_dims(images, axis=3)
        images = images / 256
        unique_labels = np.unique(labels)

        my_choice = "Nonpoint_-_Chaos_and_Earthquakes"  # "Taproot_-_Poem_Official_Video"

        prediction_anchor = np.zeros((1, matrix_size))
        print("Calculating..")

        count = 0
        predictions_song = []
        predictions_label = []
        counts = []
        distance_array = []

        for i in range(0, len(labels)):
            if labels[i] == my_choice:
                test_image = images[i]
                test_image = np.expand_dims(test_image, axis=0)
                prediction = new_model.predict(test_image)
                prediction_anchor = prediction_anchor + prediction
                count = count + 1
                print("ok")
            elif labels[i] not in predictions_label:
                predictions_label.append(labels[i])
                test_image = images[i]
                test_image = np.expand_dims(test_image, axis=0)
                prediction = new_model.predict(test_image)
                predictions_song.append(prediction)
                counts.append(1)
            elif labels[i] in predictions_label:
                index = predictions_label.index(labels[i])
                test_image = images[i]
                test_image = np.expand_dims(test_image, axis=0)
                prediction = new_model.predict(test_image)
                predictions_song[index] = predictions_song[index] + prediction
                counts[index] = counts[index] + 1

        prediction_anchor = prediction_anchor / count
        for i in range(len(predictions_song)):
            predictions_song[i] = predictions_song[i] / counts[i]
            # Cosine Similarity - Computes a similarity score of all songs with respect
            # to the anchor song.
            distance_array.append(
                np.sum(prediction_anchor * predictions_song[i])
                / (
                    np.sqrt(np.sum(prediction_anchor ** 2))
                    * np.sqrt(np.sum(predictions_song[i] ** 2))
                )
            )

        distance_array = np.array(distance_array)
        recommendations = 0

        print("Recommendation is:")

        # Number of Recommendations is set to 2.
        while recommendations < 2:
            index = np.argmax(distance_array)
            value = distance_array[index]
            print(
                "Song Name: " + predictions_label[index] + " with value = %f" % (value),
                file=sys.stderr,
            )
            distance_array[index] = -np.inf
            recommendations = recommendations + 1

        return json.dumps(unique_labels.tolist()), 201

    def load_pool(self, spectrograms_folder):
        images = []
        labels = []
        for i, (dirpath, dirnames, filenames) in enumerate(os.walk(spectrograms_folder)):
            for f in filenames:
                # song_variable = re.search('Test_Sliced_Images/.*_(.+?).jpg', f).group(1)
                # Test_Sliced_Images/3030_Chevelle_-_Send_the_Pain_Below_Official_Video.jpg
                # song_variable = f.split("/")
                # song_variable = song_variable[1]
                song_variable = f[f.index("_") + 1 : f.index(".jpg")]
                tempImg = cv2.imread(os.path.join(dirpath, f), cv2.IMREAD_UNCHANGED)
                images.append(cv2.cvtColor(tempImg, cv2.COLOR_BGR2GRAY))
                labels.append(song_variable)

            images = np.array(images)

        return images, labels