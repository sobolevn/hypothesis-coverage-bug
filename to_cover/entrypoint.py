from hypothesis import strategies as st

from to_cover.module import Example

st.register_type_strategy(Example, st.builds(Example))
