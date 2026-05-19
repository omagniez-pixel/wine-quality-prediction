# Deliverable 5 - Streamlit Mock-up

## 1. Purpose of the mock-up

The purpose of this mock-up is to show the look and feel of the future Streamlit application. It is not yet a final application connected to the complete model.

## 2. What the prototype shows

The prototype contains the following sections:

- project overview;
- simulated input form for wine characteristics;
- mocked prediction;
- presentation of the three models;
- display of the performance chart if available;
- next steps to move from mock-up to real application.

## 3. Mock inputs

The form contains fields for the physicochemical variables: acidity, residual sugar, chlorides, sulfur dioxide, density, pH, sulphates, alcohol, and wine type. These fields show how a user could enter information about a wine.

## 4. Mock prediction

The prediction is intentionally simulated. The button displays for example `Predicted quality group: medium quality`. The application clearly states that the prediction is mocked and that the final model is not connected yet.

## 5. Plan to replace mock inputs with final outputs

Plan to replace the mock-up with a real version:

- load the final preprocessing;
- load the selected model;
- transform the user inputs;
- generate a real prediction;
- display the predicted class;
- optionally display probabilities;
- integrate the final plots and metrics.

## 6. Screenshots

The screenshots were generated automatically with Playwright after launching Streamlit:

- `screenshots/streamlit_mockup_home.png`;
- `screenshots/streamlit_mockup_prediction.png`;
- `screenshots/streamlit_mockup_model_story.png`.

Command used to launch the application:

```bash
python3 -m streamlit run src/app.py --server.headless true --server.port 8501 --server.address 127.0.0.1
```
