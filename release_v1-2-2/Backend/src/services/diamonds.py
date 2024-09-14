from collections import defaultdict
from typing import Union, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database.models import Diamond, DiamondOwner


async def get_all_diamonds_with_owners(session: AsyncSession) \
        -> list[dict[str, Optional[Union[int, float, str, list[int]]]]]:
    all_diamonds_with_owners_query = (
        select(Diamond, DiamondOwner.user_id)
        .join(DiamondOwner)
        .group_by(Diamond.id, DiamondOwner.user_id)
    )

    all_diamonds_with_owners = await session.execute(all_diamonds_with_owners_query)
    diamonds_with_owners = defaultdict(lambda: {"owners": []})

    for diamond, user_id in all_diamonds_with_owners:
        diamond_dict = diamond.as_dict
        diamond_id = diamond_dict["id"]

        if diamond_id not in diamonds_with_owners:
            diamonds_with_owners[diamond_id].update(diamond_dict)

        diamonds_with_owners[diamond_id]["owners"].append(user_id)

    result = list(diamonds_with_owners.values())

    return result
