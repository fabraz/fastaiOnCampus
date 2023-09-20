from fastai.vision.all import *
import gradio as gr

learn = load_learner('export.pkl')
labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

title = "Identificador de Carro ou moto"
description = "Esse modelo tem a capacidade de identificar se uma foto contem um carro ou uma moto, envie uma imagem e aperte em submit"

gr.Interface(fn=predict, inputs=gr.inputs.Image(shape=(512, 512)), outputs=gr.outputs.Label(num_top_classes=3),title=title,description=description).launch()