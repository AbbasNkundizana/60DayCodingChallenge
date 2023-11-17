#write a python code to calculate the recovery a borehole
drawdown = float(input('Enter the dynamic water levels: '))
swl_after_pumping = float(input('Enter the static Water Level after Pumping: '))
swl_before_pumping = float(input('Enter the static Water Level before Pumping: '))



borehole_recovery = (drawdown - swl_after_pumping)/(drawdown - swl_before_pumping) *100
print(f"The recovery of the well is {round(borehole_recovery)} %")

