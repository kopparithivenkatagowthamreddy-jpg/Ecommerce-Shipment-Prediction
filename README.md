# E-Commerce Shipment Prediction

End-to-end machine learning project for predicting the shipment delivery outcome using the target `Reached.on.Time_Y.N`.

## Project Structure

```text
api/          FastAPI application
 data/raw/    Dataset
 docs/        Project documentation
 models/      Trained model and metadata
 notebooks/   Data analysis and model training notebook
 tests/       API tests
```

## Quick Start

```bash
pip install -r requirements-notebook.txt
jupyter notebook notebooks/ecommerce_shipment_analysis.ipynb
```

### Run API

```bash
pip install -r requirements-api.txt
uvicorn api.main:app --reload
```

Then visit `/docs` for interactive API documentation.
