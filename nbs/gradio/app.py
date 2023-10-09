import gradio as gr
from fastai.vision.all import *
import skimage

learn = load_learner('export.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

title = "Dogfier"
description = "Classificador raças de cachorro treinada pela Rede Neural resnet34 através da biblioteca do fastai"
examples = ['basset.jpg','border-terrier.jpg','golden-retriever.jpg','shih-tzu.jpg']
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,
             inputs=gr.inputs.Image(shape=(512, 512)),
             outputs=gr.outputs.Label(num_top_classes=3),
             title=title,
             description=description,
             examples=examples,
             interpretation=interpretation,
             enable_queue=enable_queue
).launch()