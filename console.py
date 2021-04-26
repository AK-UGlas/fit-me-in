import pdb
from models.activity import Activity
from models.location import Location
from models.member import Member

import repositories.activity_repo as act_repo
import repositories.location_repo as loc_repo
import repositories.member_repo as member_repo

# delete all submitted values and start fresh
loc_repo.delete_all()
member_repo.delete_all()

# add some members
allen = Member("Allen", "Kelly", True)
dave = Member("David", "Taylor", False)

member_repo.save(allen)
member_repo.save(dave)

# add some locations
spin_room = Location("spin room", 12)
hall1 = Location("Gym hall 1", 20)
hall2 = Location("Gym hall 2", 10)
small_room = Location("small_gym", 5)

loc_repo.save(spin_room)
loc_repo.save(hall1)
loc_repo.save(hall2)
loc_repo.save(small_room)

# return all members
all_members = member_repo.select_all()

# return a specific member
one_member = member_repo.select(allen.id)

# return all locations
all_locs = loc_repo.select_all()

# return specific location
one_loc = loc_repo.select(hall1.id)

pdb.set_trace()



