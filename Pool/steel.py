
# Legeringstilläg BE Group
# https://www.begroup.se/fileadmin/user_upload/images_and_files/Sweden/Documents_and_files_BE_Group_Sweden/Pricelist_and_stocklist/Prislistor/Legeringstillaegg/Legeringstillaegg_Augusti_2020.pdf

# Steel information for swimming pools
# https://www.imoa.info/download_files/stainless-steel/euroinox/Safe_use_swimmingpools_EN.pdf?m=1464272264&
# https://www.imoa.info/download_files/stainless-steel/Successful_Stainless_Swimming_Pool_Design.pdf

# Forumtråd fär Pool
# https://www.byggahus.se/forum/threads/svetsa-pool-i-rostfritt-stal.368708/page-2

# Some stainless steel information
# https://www.edelstahl-rostfrei.de/fileadmin/user_upload/ISER/downloads/Tables_Fabrication_Parameters_EN.pdf

# Lite pool kemikalie info
# https://www.pahlen.se/poolguiden/ph-klor/

# Some other info on chemicals and stainless types
# https://www.bssa.org.uk/topics.php?article=38
# https://www.penflex.com/chloride-chlorine-levels-and-stainless-steel-alloy-selection/
# https://www.assda.asn.au/technical-info/technical-faqs/testing-for-grade-confirmation/28-technical-info/grade-selection/271-chlorine-and-chloride--same-element,-very-different-effect





class Plate:
	def __init__(self, thickness, width, height, price_per_kg, alloy_addition_per_kg, kg_per_piece, alloy, company):
		self.thickness = thickness														# mm
		self.width = width																# mm
		self.height = height															# mm
		self.price_per_kg = price_per_kg												# kr/kg
		self.alloy_addition_per_kg = alloy_addition_per_kg								# kr/kg
		self.kg_per_piece = kg_per_piece												# kg/st
		self.alloy = alloy																# string
		self.company = company															# string

	def price_one_piece(self):
		return (self.price_per_kg + self.alloy_addition_per_kg) * self.kg_per_piece

	def price_n_pieces(self, n):
		return n * self.price_one_piece()

	def weight_one_piece(self):
		return self.kg_per_piece

	def weight_n_pieces(self, n):
		return n * self.weight_one_piece()







class RectangularTubing:
	def __init__(self, thickness, width, height, length, price_per_meter, alloy_addition_per_kg, kg_per_meter, alloy, company):
		self.thickness = thickness														# mm
		self.width = width																# mm
		self.height = height															# mm
		self.length = length															# mm
		self.price_per_meter = price_per_meter											# kr/m
		self.alloy_addition_per_kg = alloy_addition_per_kg								# kr/kg
		self.kg_per_meter = kg_per_meter												# kg/m
		self.alloy = alloy																# string
		self.company = company															# string

	def price_one_piece(self):
		return (self.length * self.price_per_meter / 1000.0) + (self.length * self.kg_per_meter * self.alloy_addition_per_kg / 1000.0)

	def price_n_pieces(self, n):
		return n * self.price_one_piece()

	def weight_one_piece(self):
		return self.kg_per_meter * self.length / 1000.0

	def weight_n_pieces(self, n):
		return n * self.weight_one_piece()








class RectangularBar:
	def __init__(self, thickness, width, length, price_per_kg, alloy_addition_per_kg, kg_per_meter, alloy, company):
		self.thickness = thickness														# mm
		self.width = width																# mm
		self.length = length															# mm
		self.price_per_kg = price_per_kg												# kr/m
		self.alloy_addition_per_kg = alloy_addition_per_kg								# kr/kg
		self.kg_per_meter = kg_per_meter												# kg/m
		self.alloy = alloy																# string
		self.company = company															# string

	def price_one_piece(self):
		return (self.price_per_kg + self.alloy_addition_per_kg) * self.kg_per_meter * self.length / 1000.0

	def price_n_pieces(self, n):
		return n * self.price_one_piece()

	def weight_one_piece(self):
		return self.kg_per_meter * self.length / 1000.0

	def weight_n_pieces(self, n):
		return n * self.weight_one_piece()





# STAINLESS STEEL (Put used ones in the top and unused ones in the bottom):
stainless_sheet = Plate(3, 1500, 3000, 47.16, 16.54, 108, '1.4462', 'BE Group')
stainless_rectangular_tubing_1 = RectangularTubing(2, 30, 30, 6000, 47.48, 16.57, 1.84, '1.4301', 'BE Group')
stainless_rectangular_tubing_2 = RectangularTubing(2, 30, 30, 6000, 79.40, 23.12, 1.84, '1.4404', 'BE Group')
stainless_flat_bar = RectangularBar(5, 30, 6000, 32.94, 17.47, 1.18, '1.4301', 'BE Group')

#underside_flat_bar = RectangularBar(4, 30, 5000, 32.94, 17.47, 0.94, '1.4301', 'BE Group')
#stainless_sheet_extra_1 = Plate(1, 1000, 2000, 22.25, 14.29, 16, '1.4301 2B', 'BE Group')
#stainless_sheet_extra_2 = Plate(1.25, 1000, 2000, 21.56, 14.29, 20, '1.4301 2B', 'BE Group')
#stainless_sheet_extra_3 = Plate(1.5, 1000, 2000, 20.32, 14.29, 24, '1.4301 2B', 'BE Group')
#stainless_sheet_extra_4 = Plate(2, 1000, 2000, 19.64, 14.29, 32, '1.4301 2B', 'BE Group')

# BLACK STEEL (Put used ones in the top and unused ones in the bottom):
rectangular_tubing_1 = RectangularTubing(3, 40, 40, 6000, 17.86, 0, 3.3, 'KKR EN10219', 'BE Group')
rectangular_tubing_2 = RectangularTubing(3, 30, 30, 6000, 17.86, 0, 2.36, 'KKR EN10219', 'BE Group')
flat_bar = RectangularBar(5, 30, 6000, 23.71, 0, 1.18, 'S235JR', 'BE Group')





def calcAndPrint():
	print('\nStainless Metal For Pool')
	#print('Inside Sheets: ',inside_plate.price_n_pieces(6))
	#print('Rectangular Tubing: ', underside_rectangular_tubing.price_n_pieces(5))
	#print('Bar: ', underside_bar.price_n_pieces(6))
	total_stainless_price = stainless_sheet.price_n_pieces(6) + stainless_rectangular_tubing_1.price_n_pieces(5) + stainless_rectangular_tubing_2.price_n_pieces(6) + stainless_flat_bar.price_n_pieces(6)
	total_stainless_weight = stainless_sheet.weight_n_pieces(6) + stainless_rectangular_tubing_1.weight_n_pieces(5) + stainless_rectangular_tubing_2.weight_n_pieces(6) + stainless_flat_bar.weight_n_pieces(6)
	print('Total Stainless Price: ', total_stainless_price)
	print('Total Stainless Weight: ', total_stainless_weight)

	print('\nBlack Steel Supports')
	#print('Big Tubing: ', rectangular_tubing_1.price_n_pieces(8))
	#print('Small Tubing', rectangular_tubing_2.price_n_pieces(4))
	#print('Bar', support_bar.price_n_pieces(6))
	total_black_steel_price = rectangular_tubing_1.price_n_pieces(8) + rectangular_tubing_2.price_n_pieces(4) + flat_bar.price_n_pieces(6)
	total_black_steel_weight = rectangular_tubing_1.weight_n_pieces(8) + rectangular_tubing_2.weight_n_pieces(4) + flat_bar.weight_n_pieces(6)
	print('Total Black Steel Price: ', total_black_steel_price)
	print('Total Black Steel Weight: ', total_black_steel_weight, '\n')

	return [total_stainless_price + total_black_steel_price, total_stainless_weight + total_black_steel_weight]




def calcMeanPressure():
	total_surface_area = (0.04 * 4 * 3) + (0.04 * 2 * 9) - (0.04 * 0.04 * 23)
	print(total_surface_area)
	total_weight = 800 + 12000 + 3000 # Steel + Water + 30 people
	return total_weight * 9.82 / total_surface_area / 1000 # in kPa

