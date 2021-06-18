import math

# main
def main():
    name = '#1 Picnic'
    radius = 6.83
    height = 10.16
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#1 Tall'
    radius = 7.78
    height = 11.91
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#2'
    radius = 8.73
    height = 11.59
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#2.5'
    radius = 10.32
    height = 11.91
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#3 Cylinder'
    radius = 10.79
    height = 17.78
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#5'
    radius = 13.02
    height = 14.29
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#6Z'
    radius = 5.40
    height = 8.89
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#8Z short'
    radius = 6.83
    height = 7.62
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#10'
    radius = 15.72
    height = 17.78
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#211'
    radius = 6.83
    height = 12.38
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#300'
    radius = 7.62
    height = 11.27
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

    name = '#303'
    radius = 8.10
    height = 11.11
    storage = storage_efficiency(cylinder_volume(radius, height), surface_area(radius, height))
    print(f'{name} {storage:.1f}')

# cylinder_volume

def cylinder_volume(radius, height):
    cylinder_volume = math.pi * radius ** 2 * height
    return cylinder_volume

# cylinder_surface_area

def surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# storage_efficiency

def storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()