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

rental = Rental(price=1000000, monthly_rent=20000, monthly_hoa=0.0, monthly_utilities=2000, \
               management_fee=0.00, tax_rate=0.02, home_ins_rate=0.007, flood_ins_rate=0.003, \
               loan_ratio=0.75, loan_term=30, loan_rate=0.085, additional_investment=150000)
rental.summarize()
```
