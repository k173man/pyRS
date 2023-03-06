---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region papermill={"duration": 0.010925, "end_time": "2019-09-24T09:49:21.794239", "exception": false, "start_time": "2019-09-24T09:49:21.783314", "status": "completed"} -->
In this notebook we plot the world population and the gross domestic product per country
<!-- #endregion -->

```python papermill={"duration": 0.020995, "end_time": "2019-09-24T09:49:21.849334", "exception": false, "start_time": "2019-09-24T09:49:21.828339", "status": "completed"} tags=["parameters"]
year = 2000
```

```python papermill={"duration": 0.013179, "end_time": "2019-09-24T09:49:21.866509", "exception": false, "start_time": "2019-09-24T09:49:21.853330", "status": "completed"} tags=["injected-parameters"]
# Parameters
year = 2017

```

```python papermill={"duration": 1.232749, "end_time": "2019-09-24T09:49:23.102994", "exception": false, "start_time": "2019-09-24T09:49:21.870245", "status": "completed"}
from plots import sundial_plot
```

<!-- #region papermill={"duration": 0.04115, "end_time": "2019-09-24T09:49:23.147805", "exception": false, "start_time": "2019-09-24T09:49:23.106655", "status": "completed"} -->
## World Population
<!-- #endregion -->

```python papermill={"duration": 1.66921, "end_time": "2019-09-24T09:49:24.825874", "exception": false, "start_time": "2019-09-24T09:49:23.156664", "status": "completed"}
sundial_plot('SP.POP.TOTL', 'World Population', year)
```

<!-- #region papermill={"duration": 0.065791, "end_time": "2019-09-24T09:49:24.957787", "exception": false, "start_time": "2019-09-24T09:49:24.891996", "status": "completed"} -->
## Gross Domestic Product (current USD)
<!-- #endregion -->

```python papermill={"duration": 0.457098, "end_time": "2019-09-24T09:49:25.475339", "exception": false, "start_time": "2019-09-24T09:49:25.018241", "status": "completed"}
sundial_plot('NY.GDP.MKTP.CD', 'Gross Domestic Product', year)
```
