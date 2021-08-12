# Notes to the presentation: Introduction to time series forecasting
> [Introduction to time series forecasting](https://youtu.be/cBojo1hsHiI)
## Introduction to Time Series Forecasting from an ML perspective
### Waht Makes Time Series Special
1. Time Series include a Timestamp
    1. Time Series Analysis
        > Involves developing models that best capture or describe an observed time series in order to understand the underlying causes
    2. Time Series Forcasting
        > Making predictions about the future is called **extrapolation** in the classical statistical handling of time series data
2. Sliding Window
    + Use of historical data in the dataset
### Python Libaries for Time Series Forcasting
+ SciPy _Ecosystem of Python libaries_
    + NumpPy        _Library that provides efficent array operations_
    + Matplotlib    _Library that provides data visualization support_
    + Pandas        _Library that provides data handling support_
        ```python
        import pandas as pd

        # CONCEPT: Date times
        # https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
        pd.to_datetime()
        # https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
        pd.date_rage()

        # CONCEPT: Time deltas
        # https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html
        pd.to_timedelta()
        # https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html
        pd.timedelta_range()

        # CONCEPT: Time Spans
        # https://pandas.pydata.org/docs/reference/api/pandas.Period.html
        pd.Period()
        # https://pandas.pydata.org/docs/reference/api/pandas.period_range.html
        pd.period_range()

        # CONCEPT: Date Offset
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset
        pd.tseries.offsets.DateOffset()
        ```
    + Statsmodels   _Library that provides time series modeling support_
    + Scikitlearn   _Library that provides machine learning support_
## Autoregressive Methods for Time Series Forecasting & Automated ML
### 11 diffrent classical time series forecasting methodes (not inclusive)
1. Autoregression _(AR)_
2. Moving Average _(MA)_
3. Autoregressive Moving Average _(ARMA)_
    + **Explenation:**
        + Autoregression _(AR)_
        > A model that uses the dependent relationship berween an observation and some number of lagged observations
        + Integrated _(I)_
        > The use of differencing of raw observations (e.g. subtracting an observation from an observation at the previous time step) in order to make the time series stationary
        + Moving Average _(MA)_
        > A model that uses the dependency between an observation and a residual error from a moving average model applied to lagged observations
    + **Parameters**
        + p  _The number of lag observation included in the model, also called the lag order_
        + d  _The number of times that the raw observations are differenced, also called the degree of differencing_
        + q  _The size of the moving average window, also called the order of moving average_
    + **Example**
    ```python
    ### Arima example ###
    from statsmodels.tsa.arima_model import ARIMA
    from random import random
    ### contrived dataset ###
    data = [x + random() for x in range(1, 100)]
    ### fit model ###
    # Define the model by calline ARIMA() and passing in the p, d, and q parameters
    model = ARIMA(data, order(1, 1, 1))
    # The model is prepared on the traning data by calling the fit() function
    model_fit = model.fit(dsip=False)
    ### Make prediction ###
    # Predictions can be made by calling the predict() function and specifying the index of the time or times to be predicted
    y_pred = model_fit.predict(len(data), len(data), typ='levels')
    print(y_pred)
    ```
4. Autoregressive Integrated Moving Average _(ARIMA)_
5. Seasonal Autoregressive Integrated Moving-Average _(SARIMA)_
6. Seasonaö Autoregressive Integrated Moving-Average with Exogenous Regressors _(SARIMAX)_
7. Vector Autoregression _(VAR)_
8. Vector Autoregression Moving-Average _(VARMA)_
9. Vector Autoregression Moving-Average with Exogenous Regressors _(VARMAX)_
10. Simple Exponential Smoothing _(SES)_
11. Holt Winter's Exponential Smoothing _(HWES)_
## Introduction to Recurremt Neural Networks _(RNN)_ for Time Series Forecasting
### Comparison Mchine Learning and Deep Leraning (Neural Networks)
|                       | Machine Learning                                                                      | Deep Learning                                                                                                                                                  |
|:----------------------|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of data points | Can use small amounts provided by users                                               | Requires a lot of unlabeled training data to make concise conclusions                                                                                          |
| Hardware dependencies | Can work on low-end machines. It does not need a large amount of computational power  | Depends on high-end machines. It inherendtly does a large amount of matrix multiplication operations. These operations can be efficently optimized using a GPU |
| Featurization process | Requires features to be accuratly identified and created by useres                    | It learn high-level features from data and creates new features by itself                                                                                      |
| Learning approch      | Divides tasks into small pieces and then combine received results into one conclusion | Solves the problem on the end-to-end basis                                                                                                                     |
| Execution Time        | Comparatively takes less time to train, ranging from a few seconds to aa few hours    | Takes a long time to train. This is because there are so many parameters in a deep learning algorithm that training them takes longe than usual                |
| Output                | The Output is usually a numerical value, like a score or a classification             | The Output can be anything from a score, a text, an element, a second                                                                                          |
### Why _RNN_
+ _RNN_ has been shown perform well in many scenarios
+ _RNN_ model is very flexible
+ _RNN_ can learn from big data
### Backpropagation through time _(BPTT)_
1. Forward through entire sequence to compute loss
2. then backward through entire sequence to compute gradient
### What are _RNNs_?
_RNN_ has internal hidden state wich can be fed back to the network
#### Unrolled _RNN_
The same weight and bias shared across all the steps
```python
model = Sequential()
model.add(RNN(4, input_shape=(timesteps, data_dim))
model.add(Dense(3, activation='softmax'))
```
## Example
### Resources
> https://github.com/FrancescaLazzeri/Machine-Learning-for-Time-Series-Forecasting