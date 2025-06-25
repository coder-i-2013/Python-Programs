import tkinter as tk
from tkinter import ttk
import requests

# API URL for fetching recipes
API_URL = "https://www.themealdb.com/api/json/v1/1/search.php?s="

favorites = set()  # Store favorite dishes

# Function to search recipes dynamically
def search_recipes():
    query = search_entry.get().strip()
    if not query:
        results_list.delete(0, tk.END)
        results_list.insert(tk.END, "Please enter a dish name!")
        return
    
    response = requests.get(API_URL + query)
    data = response.json()
    
    results_list.delete(0, tk.END)  # Clear previous results
    
    if data["meals"]:
        for meal in data["meals"]:
            results_list.insert(tk.END, meal["strMeal"])  # Show dish names
    else:
        results_list.insert(tk.END, "No recipes found!")

# Function to show full recipe details
def show_recipe(event):
    selected_recipe = results_list.get(results_list.curselection())
    response = requests.get(API_URL + selected_recipe)
    data = response.json()
    
    if data["meals"]:
        meal = data["meals"][0]
        recipe_text.delete("1.0", tk.END)
        recipe_text.insert(tk.END, f"🍽️ {meal['strMeal']}\n\n")
        recipe_text.insert(tk.END, f"🌍 Cuisine: {meal['strArea']}\n")
        recipe_text.insert(tk.END, f"📖 Instructions:\n{meal['strInstructions']}\n\n")
        recipe_text.insert(tk.END, "🥣 Ingredients:\n")
        
        for i in range(1, 21):  # Fetch up to 20 ingredients
            ingredient = meal[f"strIngredient{i}"]
            measurement = meal[f"strMeasure{i}"]
            if ingredient and ingredient.strip():
                recipe_text.insert(tk.END, f"- {measurement} {ingredient}\n")
    else:
        recipe_text.delete("1.0", tk.END)
        recipe_text.insert(tk.END, "Recipe details not found!")

# Function to add to favorites
def add_to_favorites(event):
    selected_recipe = results_list.get(results_list.curselection())
    if selected_recipe and selected_recipe != "No recipes found!":
        favorites.add(selected_recipe)
        update_favorites()

# Function to update favorites list
def update_favorites():
    favorites_list.delete(0, tk.END)
    for recipe in favorites:
        favorites_list.insert(tk.END, recipe)

# Function to switch screens
def show_home():
    home_frame.pack(fill="both", expand=True)
    favorites_frame.pack_forget()

def show_favorites():
    favorites_frame.pack(fill="both", expand=True)
    home_frame.pack_forget()

# Main window setup
root = tk.Tk()
root.title("Global Recipe Finder")
root.geometry("600x500")

# Top navigation bar
nav_bar = tk.Frame(root, bg="lightgray")
nav_bar.pack(fill="x")

home_btn = tk.Button(nav_bar, text="Home", command=show_home)
home_btn.pack(side="left", padx=10, pady=5)

favorites_btn = tk.Button(nav_bar, text="Favorites", command=show_favorites)
favorites_btn.pack(side="left", padx=10, pady=5)

# Home Screen
home_frame = tk.Frame(root)
home_frame.pack(fill="both", expand=True)

search_label = tk.Label(home_frame, text="Enter a dish:")
search_label.pack(pady=5)

search_entry = tk.Entry(home_frame)
search_entry.pack(pady=5)

search_btn = tk.Button(home_frame, text="Search", command=search_recipes)
search_btn.pack(pady=5)

results_list = tk.Listbox(home_frame, width=50, height=10)
results_list.pack(pady=5)
results_list.bind("<Double-Button-1>", add_to_favorites)  # Double-click to add to favorites
results_list.bind("<ButtonRelease-1>", show_recipe)  # Click to show full recipe

recipe_text = tk.Text(home_frame, width=60, height=10, wrap="word")
recipe_text.pack(pady=5)

# Favorites Screen
favorites_frame = tk.Frame(root)

favorites_label = tk.Label(favorites_frame, text="Favorite Recipes:")
favorites_label.pack(pady=5)

favorites_list = tk.Listbox(favorites_frame, width=50, height=10)
favorites_list.pack(pady=5)

# Start with Home Screen
show_home()

root.mainloop()