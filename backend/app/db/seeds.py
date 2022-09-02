import asyncio
import os
import random
import string
import asyncpg

from app.db.repositories.comments import CommentsRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.users import UsersRepository

def randomword(length):
    return ''.join(random.choice(string.printable) for _ in range(length))


async def seed_db() -> None:
    conn = await asyncpg.connect(os.getenv('DATABASE_URL'))

    # 100 users
    users = []
    users_repo = UsersRepository(conn)
    for index in range(100):
        user = await users_repo.create_user(
            username=f'browniebroke{index}',
            email=f'cookie{index}@browniebroke.com',
            password=randomword(12),
        )
        users.append(user)

    # 100 items
    items = []
    items_repo = ItemsRepository(conn)
    foods = [
        ('Pizza', 'Dough with tomatoe & cheese'),
        ('Pasta', 'Various shaped with sauce and sometimes cheese'),
        ('Stew', 'Some meat and vegetables in a sauce'),
        ('Panini', 'Sandwich with cheese and vegetables'),
        ('Salad', 'Vegetables with dressing'),
        ('Soup', 'Vegetables in a broth'),
        ('Burger', 'Meat in a bun with cheese and vegetables'),
        ('Sandwich', 'Meat in a bun with cheese and vegetables'),
        ('Tacos', 'Meat in a tortilla with cheese and vegetables'),
        ('Burrito', 'Meat in a tortilla with cheese and vegetables'),
        ('Sushi', 'Fish in a rice roll with vegetables'),
        ('Ramen', 'Noodles in a broth with vegetables'),
    ]
    for index in range(100):
        title, desc = random.choice(foods)
        item = await items_repo.create_item(
            slug=f'{title.lower()}-{index}',
            title=f'{title} {index}',
            description=desc,
            seller=random.choice(users),
        )
        items.append(item)

    # 100 comments
    comments = []
    comments_repo = CommentsRepository(conn)
    for index in range(100):
        comment = await comments_repo.create_comment_for_item(
            body=randomword(100),
            item=random.choice(items),
            user=random.choice(users),
        )
        comments.append(comment)

    # Close the connection
    await conn.close()


asyncio.run(seed_db())
