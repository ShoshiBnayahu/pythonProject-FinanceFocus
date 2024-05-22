from app.routes import user_action_router
import matplotlib.pyplot as plt
from app.services import user_action_service, user_service


async def get_user_monthly_sums(user_id: int, year: int):
    """
       Calculate the total sums of user actions by month for a given year.
       Args:
       user_id (int): The user ID.
       year (int): The year for the calculations.
       Returns:
       tuple: Lists of months and corresponding monthly sums.
       """
    await user_service.get_user_by_id(user_id)
    months = list(range(1, 13))
    monthly_sums = []
    for m in months:
        user_actions = await user_action_router.get_user_actions_by_month(user_id, year, m)
        total_sum = sum(-u.amount if u.type == 'revenue' else u.amount for u in user_actions)
        monthly_sums.append(total_sum)
    return months, monthly_sums


def create_plot(month, sums):
    """
        Create a line plot of monthly sums.
        Args:
        month (list): List of months.
        sums (list): List of sums for each month.
        Returns:
        matplotlib.figure.Figure: The plot figure.
        """
    plt.figure()
    plt.plot(month, sums)
    plt.xlabel('Month')
    plt.ylabel('Sum')
    plt.title('User Monthly Sums')
    plt.grid(True)
    plt.tight_layout()
    return plt.show()

async def get_user_monthly_by_type(user_id: int, action_type: str):
    """
        Calculate the total amounts of user actions by type and month.
        Args:
        user_id (int): The user ID.
        action_type (str): The type of actions (e.g., 'expense', 'revenue').
        Returns:
        tuple: Lists of months and corresponding monthly amounts.
        """
    await user_service.get_user_by_id(user_id)
    months = list(range(1, 13))
    monthly_amounts = []
    for month in months:
        actions_filtered = await user_action_service.get_user_actions_by_type_in_month(user_id, action_type, month)
        total_amounts = sum(-action.amount if action.type == 'expense' else action.amount for action in actions_filtered)
        monthly_amounts.append(total_amounts)
    return months, monthly_amounts