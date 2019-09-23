# Ratesheet parsing

## Challenge

### Parser
#### Format
* Mutipal format (pdf, xml, excel, html)
* Adjustment: table format, list format
#### Change format
* Change frequently
* Handle failure
#### Multi state
Some lender publish rate and adj for each state
#### Heavy Business logic
* lender define diffent program adj. Some special adj apply short spefic case break format of ratesheet file
* many loans type: comfi, jumbo, ...

### Quote engine
#### Performence
* quote many lenders/time
* Lender has many rates
* Rate can be apply many adj base on user profile
--> easy to hit perf issue
#### Verify
* Hard to proven that quote engine is correct

## Requirement:
* Manage mutipal format
* Handle format change quickly
* Provide the way to define meta data to ratesheet. Easy to share with non-tech people
* Quote engine: Calculate many lenders parallel
* Adj breakdown: after calculate rate, should have explain why we have this result
* If format change, need to fix without deploy new version ***(*)***
## Suggest tech stack
### Java
### Spring

## API
### List of supported lenders:
```
GET: api/v1.0/lenders
```
### Get quote for lender
```
POST: api/v1.0/quote/lender/${lenderId}
```
With body with json parrams have these attributes:
* credit_score: Credit score
* has_equity_loan: Already has loan
* loan_amount: Loan amount
* property_value: Property value
* loan_program: 25-Yr Fixed or 25-arm
* loan_type: Conventional/FHA/VA/USDA
* occupancy: Owner/Investment/Second Home
* property_type: Single Family Resident/Condominium...
* purpose: Refinance/Purchase Mortgage/Cash-out
* zipcode: property zipcode

