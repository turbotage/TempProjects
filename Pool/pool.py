
import steel
import styrofoam

# BROKEN
def lost_temperature(loss_effect, water_amount, time):
	return time * loss_effect / (4190 * water_amount)

# BROKEN
def calcTimePerDegreeLost(pool_temp, i):
	timestamp = 3600 # 30 min
	outside_temp = 5
	temp_diff = pool_temp - outside_temp
	if (abs(temp_diff) < 0.1) or (i > 100):
		return [i * timestamp / 60 / 60, pool_temp] # [Time in min, Pool Temperature]

	loss_effect = 10*styrofoam.calcEffectDT(temp_diff) + 60*temp_diff
	#print(loss_effect,'\n')
	pool_temp = pool_temp - lost_temperature(loss_effect, 11000, timestamp)
	#print(pool_temp,'\n')
	return calcTimePerDegreeLost(pool_temp, i+1)




print(steel.calcAndPrint())

print(steel.calcMeanPressure())


print(styrofoam.calcAndPrint())

print(styrofoam.calcEffect())


print(calcTimePerDegreeLost(15, 0))