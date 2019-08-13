import numpy as np, seaborn as sns, matplotlib.pyplot as plt

flights=sns.load_dataset('flights')

mth_tot=flights.groupby('month').sum()['passengers'].reset_index()

pal=sns.color_palette("Blues_d",len(mth_tot))

rank=mth_tot['passengers'].argsort().argsort()

pl=sns.barplot(x='month',y='passengers',data=flights,estimator=sum,ci=None,palette=np.array(pal[::-1])[rank])
pl.set_title('Total Passengers by Months')

for indx, row in mth_tot.iterrows():
    pl.text(row.name,row.name,row.passengers,color='black',ha='center')
    #print(row)

plt.show()
