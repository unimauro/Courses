import pandas as pd
game_df = pd.read_csv("game.csv")
plays_df = pd.read_csv("game_plays.csv")
plays_df = plays_df.drop(['secondaryType', 'periodType',
'dateTime', 'rink_side'], axis=1).fillna(0)

import featuretools as ft
from featuretools import Feature
es = ft.EntitySet(id="plays")


es = es.entity_from_dataframe(entity_id="plays",dataframe=plays_df
,index="play_id", variable_types = {
"event": ft.variable_types.Categorical,
"description": ft.variable_types.Categorical })
f1 = Feature(es["plays"]["event"])
f2 = Feature(es["plays"]["description"])
encoded, defs = ft.encode_features(plays_df, [f1, f2], top_n=10)
encoded.reset_index(inplace=True)
encoded.head()

es = ft.EntitySet(id="plays")
es = es.entity_from_dataframe(entity_id="plays",
dataframe=encoded, index="play_id")
es = es.normalize_entity(base_entity_id="plays",
new_entity_id="games", index="game_id")
features,transform=ft.dfs(entityset=es,
target_entity="games",max_depth=2)
features.reset_index(inplace=True)
features.head()


