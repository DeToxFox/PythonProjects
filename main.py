# St. John's Marina & Yacht Club Yearly Member Receipt Generator Program

# Written by: David Turner
# Date written: Jan 28, 2022
# Project ID: QAP-2, Project 1: St. John's Marina & Yacht Club Receipt Program


# Constants
EVEN_SITES_COST = 80.00
ODD_SITES_COST = 120.00
ALT_MEM_COST = 5.00
CLEANING_COST = 50.00
VID_SURV_COST = 35.00
HST_PERCENT = 0.15
STAND_DUE_COST = 75.00
EXEC_DUE_COST = 150.00
PROCESS_FEE = 59.99
CANCEL_PERCENT = 0.60

# Inputs
CustName = input("Enter the customer name: ").upper()
StAdd = input("Enter the street address: ").upper()
City = input("Enter the city name: ").upper()
Prov = input("Enter the province (XX): ").upper().upper()
Postal = input("Enter the postal code (XXXXXX): ").upper()
HomePhone = input("Home phone number (1231231234): ")
CellPhone = input("Cell phone number (1231231234): ")
SiteNum = int(input("Please enter a site number (1-100): "))
MemberType = input("Member type Standard or Executive (S/E): ").upper()
AltMembers = int(input("Number of Alternate members: "))
WkCleaning = input("Weekly site cleaning, Yes/No (Y/N): ").upper()
VidSurv = input("Video Surveillance, Yes/No (Y/N): ").upper()

# Determining and calculating site charges
EvenOdd = SiteNum % 2
if EvenOdd == 0:  # Even
    SiteCharge = EVEN_SITES_COST + (AltMembers * ALT_MEM_COST)
else:  # Odd
    SiteCharge = ODD_SITES_COST + (AltMembers * ALT_MEM_COST)

# Evaluating and calculating extra charges
if WkCleaning == "Y" and VidSurv == "Y":
    ExtraCharge = CLEANING_COST + VID_SURV_COST
    WkCleaningDsp = "YES"
    VidSurvDSP = "YES"
elif WkCleaning == "Y" and VidSurv == "N":
    ExtraCharge = CLEANING_COST
    WkCleaningDsp = "YES"
    VidSurvDSP = "NO"
elif VidSurv == "Y" and WkCleaning == "N":
    ExtraCharge = VID_SURV_COST
    WkCleaningDsp = "NO"
    VidSurvDSP = "YES"
else:
    ExtraCharge = 0
    WkCleaningDsp = "NO"
    VidSurvDSP = "NO"

# Calculate subtotal adding site charges and extra charges together
SubTotal = SiteCharge + ExtraCharge

# Calculate HST
Total_HST = SubTotal * HST_PERCENT

# Calculate Total monthly charges
TotMonCharge = SubTotal + Total_HST

# Calculate Total monthly dues $75 for std and $150 for executive
if MemberType == "S":
    MonDues = STAND_DUE_COST
    MemberTypeDsp = "STANDARD"
else:
    MonDues = EXEC_DUE_COST
    MemberTypeDsp = "EXECUTIVE"

# Calculate Total monthly charge
TotMonFee = MonDues + TotMonCharge

# Calculate total Yearly Fees  Total monthly fee * 12
TotalYearFee = TotMonFee * 12

# Calculate total monthly payment
MonPaym = (TotalYearFee + PROCESS_FEE) / (12)

# Calculate Cancellation Fee, 60% of the yearly site charges
CanFee = (SiteCharge * 12) * CANCEL_PERCENT

# Variables that require specific formatting related to currency
SiteChargeDsp = "${:,.2f}".format(SiteCharge)
ExtraChargeDsp = "${:,.2f}".format(ExtraCharge)
SubTotalDsp = "${:,.2f}".format(SubTotal)
Total_HSTDsp = "${:,.2f}".format(Total_HST)
TotMonChargeDsp = "${:,.2f}".format(TotMonCharge)
MonDuesDsp = "${:,.2f}".format(MonDues)
TotMonFeeDsp = "${:,.2f}".format(TotMonFee)
TotalYearFeeDsp = "${:,.2f}".format(TotalYearFee)
MonPaymDsp = "${:,.2f}".format(MonPaym)
CanFeeDsp = "${:,.2f}".format(CanFee)

print()
print(" "*3, "St. John's Marina & Yacht Club")
print(" "*7, "Yearly Member Receipt")
print("-"*38)
print()
print("Client Name and Address:")
print()
print("{:<24}".format(CustName))
print("{:<24}".format(StAdd))
print("{:<15}".format(City + ", " + Prov + " " + Postal))
print()
print("Phone: {:<10}".format(HomePhone + " (H)"))
print("       {:<10}".format(CellPhone + " (C)"))
print()
print("Site #: {:<3}   Member type: {:>9}".format(SiteNum, MemberTypeDsp))
print()
print("{:<33} {:>2}".format("Alternate members:", AltMembers))
print("{:<32} {:>3}".format("Weekly site cleaning:", WkCleaningDsp))
print("{:<32} {:>3}".format("Video surveillance:", VidSurvDSP))
print()
print("{:<26} {:>9}".format("Site charges:", SiteChargeDsp))
print("{:<28} {:>7}".format("Extra charges:", ExtraChargeDsp))
print(" "*25, "-"*11)
print("{:<26} {:>9}".format("Subtotal:", SubTotalDsp))
print("{:<28} {:>7}".format("Sales tax (HST):", Total_HSTDsp))
print(" "*25, "-"*11)
print("{:<26} {:>9}".format("Total monthly charges:", TotMonChargeDsp))
print("{:<28} {:>7}".format("Monthly dues:", MonDuesDsp))
print(" "*25, "-"*11)
print("{:<26} {:>9}".format("Total monthly fees:", TotMonFeeDsp))
print("{:<25} {:>10}".format("Total yearly fees:", TotalYearFeeDsp))
print(" "*25, "-"*11)
print("{:<26} {:>9}".format("Monthly payment:", MonPaymDsp))
print()
print("-"*38)
print()
print("Issued: 2022-01-29")
print("HST Reg No: 549-33-5849-4720-9885")
print()
print("{:<26} {:>9}".format("Cancellation fee:", CanFeeDsp))
print("-"*38)