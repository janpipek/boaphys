import boaphys

print(boaphys.astronomy.Earth.escape_velocity)
print(boaphys.astronomy.Sun.escape_velocity)
print(boaphys.astronomy.Earth.surface_gravity)

print(boaphys.astronomy.schwarzchild_radius(boaphys.astronomy.Sun))
print(boaphys.astronomy.schwarzchild_radius(boaphys.astronomy.Earth))
