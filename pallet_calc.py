area_needed = float(input('HOW MANY SQUARE METERS DO YOU NEED: '))
print('ENTER PALLET DIMENSIONS:')

pallet_length = float(input('Length [cm]: '))
pallet_width = float(input('Width [cm]: '))

pallet_area = (pallet_length * pallet_width) / 10000

pallet_price = float(input('Enter price per pallet (PLN): '))

print(f'\nPALLET DIMENSIONS\nLength: {pallet_length} cm\nWidth: {pallet_width} cm\nArea: {pallet_area} m²')

pallet_count = area_needed / pallet_area
total_cost = pallet_count * pallet_price

print(f'\nYou will need approximately {pallet_count:.2f} pallets.')
print(f'Total cost: {total_cost} PLN')
