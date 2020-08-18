
import math

class Styrofoam:
	def __init__(self, thickness, width, height, heat_conductivity, price_per_package, pieces_per_package, styrofoam_type, company):
		self.thickness = thickness
		self.width = width
		self.height = height
		self.heat_conductivity = heat_conductivity
		self.price_per_package = price_per_package
		self.pieces_per_package = pieces_per_package
		self.styrofoam_type = styrofoam_type
		self.company = company

	def price_n_m2(self, n):
		area_per_package = self.width / 1000 * self.height / 1000 * self.pieces_per_package
		n_packages = math.ceil(n / area_per_package)
		return n_packages * self.price_per_package

	def watts_n_m2(self, n, dt):
		return self.heat_conductivity * n * dt / (self.thickness / 1000)



base = Styrofoam(50, 585, 1185, 0.037, 599, 8, 'XPS 500SL', 'e-byggstore.se')
base_area = 2.4*4.5

walls = Styrofoam(100,600,1200,0.038, 339, 5,'S80', 'e-byggstore.se')
wall1_area = 2.2*1.6
wall2_area = 4.2*1.6

def calcAndPrint():
	return base.price_n_m2(base_area) + walls.price_n_m2(wall1_area * 2 + wall2_area * 2)

# 5, 18, 30
def calcEffect():
	watts1 = base.watts_n_m2(base_area, 5) +  walls.watts_n_m2(wall1_area * 2 + wall2_area * 2, 5)
	watts2 = base.watts_n_m2(base_area, 18) + walls.watts_n_m2(wall1_area * 2 + wall2_area * 2, 18)
	watts3 = base.watts_n_m2(base_area, 30) + walls.watts_n_m2(wall1_area * 2 + wall2_area * 2, 30)
	return [watts1, watts2, watts3]

def calcEffectDT(dt):
	return base.watts_n_m2(base_area, dt) +  walls.watts_n_m2(wall1_area * 2 + wall2_area * 2, dt)
