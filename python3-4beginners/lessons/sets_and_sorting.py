def belt_color_count(dictionary):
  belts = list(dictionary.values())
  for belt in set(belts):
    num = belts.count(belt)
    print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
  ninja_name = input('enter a ninja name: ')
  ninja_belt = input('enter a ninja belt: ')
  ninja_belts[ninja_name] = ninja_belt

  another = input('Do you want to add another?(y/n)')
  if another == 'y':
    continue
  else:
    break

belt_color_count(ninja_belts)
