# 🌿 Classificação de Doenças em Plantas com Visão Computacional

Este projeto aplica técnicas de Visão Computacional e Deep Learning para identificar doenças em plantas agrícolas a partir de imagens. Utilizando modelos pré-treinados e aumento de dados, a solução atinge **92% de acurácia** na classificação de 15 diferentes classes de condições em lavouras de tomate, batata e pimentão.

---

## 🎯 Objetivo

Desenvolver um modelo capaz de classificar automaticamente doenças em folhas de plantas, auxiliando produtores no monitoramento preventivo de lavouras com base em imagens.

---

## 🧠 Tecnologias e Bibliotecas

- Python 3.10+
- TensorFlow / Keras
- OpenCV
- NumPy, Matplotlib, Scikit-learn
- Streamlit (opcional)

---

## 🖼️ Dataset

Foi usado o [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease), que contém milhares de imagens rotuladas de folhas de plantas em diferentes estágios de saúde ou infecção.

---

## ⚙️ Arquitetura do Modelo

- **Base:** MobileNetV2 (pré-treinada no ImageNet)
- **Camadas adicionais:**
  - GlobalAveragePooling2D
  - Dense(128, ReLU)
  - Dense(final, Softmax)
- **Aumento de dados:** rotação, deslocamento, zoom, espelhamento horizontal

---

## 📊 Resultados

- **Acurácia geral:** 92%
- **F1-score macro:** 91%
- **Precisão média ponderada:** 92%

Exemplo de desempenho por classe:

|  Classe                                 |  precision  |  recall |  f1-score  | support

              Pepper__bell___Bacterial_spot       0.98      0.94      0.96       183
                     Pepper__bell___healthy       0.98      0.98      0.98       285
                      Potato___Early_blight       0.97      0.96      0.97       229
                       Potato___Late_blight       0.95      0.91      0.93       230
                           Potato___healthy       0.89      0.91      0.90        34
                      Tomato_Bacterial_spot       0.96      0.96      0.96       463
                        Tomato_Early_blight       0.86      0.68      0.76       200
                         Tomato_Late_blight       0.92      0.90      0.91       411
                           Tomato_Leaf_Mold       0.74      0.98      0.84       215
                  Tomato_Septoria_leaf_spot       0.92      0.88      0.90       376
Tomato_Spider_mites_Two_spotted_spider_mite       0.84      0.93      0.88       335
                        Tomato__Target_Spot       0.76      0.88      0.82       291
      Tomato__Tomato_YellowLeaf__Curl_Virus       0.98      0.97      0.97       669
                Tomato__Tomato_mosaic_virus       0.93      0.92      0.93        77
                             Tomato_healthy       1.00      0.83      0.90       330

                                   accuracy                           0.92      4328
                                  macro avg       0.91      0.91      0.91      4328
                               weighted avg       0.92      0.92      0.92      4328


## ▶️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/lavoura-vision.git
cd lavoura-vision





