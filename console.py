import pdb, dateutil, random
from datetime import datetime, timedelta
from models.activity import Activity
from models.location import Location
from models.member import Member

import repositories.activity_repo as act_repo
import repositories.location_repo as loc_repo
import repositories.member_repo as member_repo

# delete all submitted values and start fresh
loc_repo.delete_all()
member_repo.delete_all()
act_repo.delete_all()

# add some members
allen = Member("Allen", "Kelly", "allen@kelly.com", True)
dave = Member("David", "Taylor", "dt@taylor.com", False)

member_repo.save(allen)
member_repo.save(dave)

# add some locations
spin_room = Location("Spin room", 12)
hall1 = Location("Gym hall 1", 20)
hall2 = Location("Gym hall 2", 10)
small_room = Location("Small gym", 5)

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

# set up some activities for demonstration
today = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0) 

# generate a list of timedelta objects of increasing size
times = []
for hour in range(0, 14, 1):
    times.append(timedelta(minutes=60 * hour))

act1 = Activity("Yoga", today, hall2)
act2 = Activity("Boxfit", today, hall1)
act3 = Activity("Spin", today, spin_room)
act4 = Activity("Cross-fit", today, small_room)
act5 = Activity("Step", today, hall1)
act6 = Activity("BodyPump", today, hall2)
act7 = Activity("Spin", today, spin_room)
act8 = Activity("BodyPump", today, hall1)
act9 = Activity("Yoga", today, small_room)
act10 = Activity("Salsa", today, hall2)
act11 = Activity("Spin", today, spin_room)

all_activities = [act1, act2, act3, act4, act5, 
                 act6, act7, act8, act9, act10,
                 act11]

days = 0

while days < 7:
    for activity in all_activities:
        # assign a random time to an activity
        activity.start = today + random.choice(times)
        act_repo.save(activity)

    days += 1
    today += timedelta(days=1)

pdb.set_trace()


