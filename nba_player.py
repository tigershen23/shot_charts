import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# James Harden's 2014-2015 shot chart data URL
shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201935&Plu'\
                'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
                'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                'owZones=0'

# Get data from URL
response = requests.get(shot_chart_url)
headers = response.json()['resultSets'][0]['headers']
shots = response.json()['resultSets'][0]['rowSet']

# Create pandas DataFrame from shots
shot_df = pd.DataFrame(shots, columns=headers)
# from IPython.display import display
# with pd.option_context('display.max_columns', None):
#     display(shot_df.head())

from matplotlib.patches import Circle, Rectangle, Arc

# Draw a basketball court
def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # Plot onto current axes
    if ax is None:
        ax = plt.gca()

    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    key_outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    key_inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)

    free_throw_top_arc = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    free_throw_bottom_arc = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color, linestyle='dashed')

    restricted_area = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)

    right_corner_three_line = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
    left_corner_three_line = Rectange((220, -47.5), 0, 140, linewidth=lw, color=color)

    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)

    center_court_outer_arc = Arc((0, 395), 120, 120, theta1=180, theta2=0,
                                    linewidth=lw, color=color)
    # center_court_inner_arc =

    court_elements = [hoop, backboard, outer_box]

    # if outer_lines:
        # Draw half-court line, baseline, sidelines

    # Draw elements
    for element in court_elements:
        ax.add_patch(element)

    return ax

sns.set_style("white")
sns.set_color_codes()
plt.figure(figsize=(12,11))
draw_court(outer_lines=True)
plt.xlim(-300, 300)
plt.ylim(-100, 500)
# plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)
plt.show()
