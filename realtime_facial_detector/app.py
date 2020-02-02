import time
import edgeiq
from pprint import pprint
"""
Use object detection to detect human faces in the frame in realtime.

To change the computer vision model, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_model.html

To change the engine and accelerator, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_engine_and_accelerator.html
"""

#def countVariChanger(word,counter):
#    if counter < :
#        counter = counter

def main():
    facial_detector = edgeiq.ObjectDetection(
            "alwaysai/res10_300x300_ssd_iter_140000")
    facial_detector.load(engine=edgeiq.Engine.DNN)

    print("Engine: {}".format(facial_detector.engine))
    print("Accelerator: {}\n".format(facial_detector.accelerator))
    print("Model:\n{}\n".format(facial_detector.model_id))

    fps = edgeiq.FPS()

    try:
        with edgeiq.WebcamVideoStream(cam=0) as webcam, \
                edgeiq.Streamer() as streamer:
            # Allow webcam to warm up
            time.sleep(2.0)
            fps.start()
            counter = 1
            counterWord = 0
            WordList = ['Beautiful!', 'Lovely!' , 'Amazing!' , 'Charming!' , 'Gorgeous!' , 'Heavenly!' , 'Stunning!' , 'Wow!!!' , 'Perfect!' , 'Flawless!' , 'OMG!']

            # loop detection
            while True:
                frame = webcam.read()
                # detect human faces
                results = facial_detector.detect_objects(
                        frame, confidence_level=.5)
                predictions_edit = results.predictions
                #print(str(results.predictions[0]))
                counter = counter + 1
                if counter > 100:
                    counter = 1
                    counterWord = (counterWord + 1)%(len(WordList))
                for prediction in results.predictions:
                    prediction.confidence = 1
                    #prediction.label = "Stunning"
                    prediction.label = WordList[counterWord]
                #for i in range(len(results.predictions)):
                    #results.predictions[i].confidence = 1
                    #prediction.label = "Stunning"
                    #results.predictions[i].label = WordList[(counterWord+i)%11]
                frame = edgeiq.markup_image(
                        frame, results.predictions)
				#frame = edgeiq.markup_image(frame)

                # Generate text to display on streamer
                text = ["Model: {}".format(facial_detector.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Stunning People:")

                for prediction in results.predictions:
                    #text.append("{:2.2f}%".format(prediction.confidence * 100))
                    text.append("{:2.2f}%".format(100))

                streamer.send_data(frame, text)
				#streamer.send_data(frame, text)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        # stop fps counter and display information
        fps.stop()
        print("[INFO] elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
