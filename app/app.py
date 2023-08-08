import streamlit as st
import pandas as pd
import os
from honeybee.model import Model
from pollination_streamlit_io import get_hbjson, send_hbjson

st.header('Send Room data to excel')
st.info(
    'This app takes a Pollination model and sends room properties to excel'
)

model = get_hbjson(
    key='get-po-model', label='Get Pollination Model',
    options={'selection': {'selected': True}}
)

if model:
    model: Model = Model.from_dict(model['hbjson'])

    # Create a list to hold the room properties
    room_properties = []

    for room in model.rooms:
        room_properties.append({
                'Name': room.display_name,
                'Area': room.floor_area,
                'Height': room.average_floor_height,
                'Volume': room.volume,
                'Exterior Wall Area': room.exterior_wall_area,
                'Exterior Aperture Area': room.exterior_aperture_area,
                'Exterior Wall Aperture Area': room.exterior_wall_aperture_area,
                'Exterior Skylight Aperture Area': room.exterior_skylight_aperture_area,
                'Story': room.story,
                'Multiplier': room.multiplier,
                'Exclude Floor Area': room.exclude_floor_area,
                'Geometry': room.geometry,
                'Volume': room.volume,
                'Floor Area': room.floor_area,
                'Exposed Area': room.exposed_area,
                'Exterior Wall Area': room.exterior_wall_area,
                'Exterior Aperture Area': room.exterior_aperture_area,
                'Exterior Wall Aperture Area': room.exterior_wall_aperture_area,
                'Exterior Skylight Aperture Area': room.exterior_skylight_aperture_area,
            })

    df = pd.DataFrame(room_properties)
    excel_file = 'room_properties.xlsx'
    df.to_excel(excel_file, index=False)

    st.markdown(f"**[Download Excel File]({excel_file})**")

    st.success(
        'Exported room properties to Excel. You can download the file using the link above.'
    )

    os.system(excel_file)
