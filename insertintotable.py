from main import User,engine
from sqlalchemy.orm import Session

session=Session(bind=engine)

new_user=User(username='vicky',email='vicky@gmail.com')
new_user1=User(username='pooja',email='pooja@gmail.com')
new_user2=User(username='shreya',email='shreya@gmail.com')


new_user=[
    {
        'username':'vickys','email':'vivekps@gmail.com'
    },{
        'username':'shreyaa','email':'shreyaa@gmail.com'
    },{
        'username':'poojas','email':'poojas@gmail.com'
    }
]
#session.add_all([new_user,new_user1,new_user2])
session.add(new_user)
session.commit()
"""for U in new_user:
    print(U['username'])"""