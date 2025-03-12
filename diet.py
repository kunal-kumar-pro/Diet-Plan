import streamlit as st 

st.title("Diet Plan")
st.divider()
st.subheader("Breakfast")
st.markdown("""
1. 2 boiled eggs: 156 kcal (78 kcal each)
2. 2 whole wheat bread slices: 150 kcal (75 kcal each)
3. 1 tsp butter: 34 kcal
4. 1 cup tea (with milk/sugar): ~30 kcal
5. 1 banana: 100 kcal   
6. :blue[Total Breakfast: 470 kcal]
""")
st.divider()
st.subheader("Lunch")
st.markdown("""
1. 100g cooked rice: 130 kcal
2. 50g paneer: ~133 kcal or 100g chicken: ~165 kcal
3. 1 tsp ghee/oil: 45 kcal
4. 100g boiled vegetables: ~65 kcal
5. 100g curd: 65 kcal
6. :blue[Total Lunch (Paneer): 437 kcal]
7. :blue[Total Lunch (Chicken): 470 kcal]
""")
st.divider()
st.subheader("Evening Snack")
st.markdown("""
1. 1 handful almonds (28g): ~165 kcal
2. 1 cup green tea: ~2 kcal
3. 1 small apple: ~80 kcal
4. :blue[Total Snack: 247 kcal]
""")
st.divider()
st.subheader("Dinner")
st.markdown("""
1. 2 chapatis: 150 kcal (75 kcal each)
2. 100g dal: ~120 kcal
3. 1 tsp ghee: 45 kcal
4. 50g salad: ~15 kcal
5. 50g curd: ~33 kcal
6. :blue[Total Dinner: 363 kcal]
""")
st.divider()
st.header("Total Daily Calorie Intake")
st.subheader(""":green[With Paneer: ~1,517 kcal]""")
st.subheader(""":red[With Chicken: ~1,550 kcal]""")