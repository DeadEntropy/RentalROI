RentalROI
====================

This package can be used to analyse rental properties ROI


Installation
--------------------

To install RentalROI, simply:

```commandline
pip install rentalroi
```


How To Use
--------------------

Start by importing the Rental class 

```python
from rentalroi.rental import Rental

```

Then create a rental object a view a summary

```python
from rentalroi.rental import Rental

rental = Rental(price=130000, rent=1900, hoa=267, management_fee=0.00, tax_rate=0.0112, insurance_rate=0.004, \
                loan_ratio=0.80, loan_term=15, loan_rate=0.06, additional_investment=20000)
rental.summarize()
```
