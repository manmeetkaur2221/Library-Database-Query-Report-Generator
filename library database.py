
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random
from IPython.display import display, HTML, clear_output

# Pastel theme
pastel_green = "#A8E6CF"
pastel_pink = "#FFB6B9"
accent = "#F6F1FF"
sns.set_style("whitegrid")

plt.rcParams["figure.facecolor"] = "#ffffff"
plt.rcParams["axes.facecolor"] = "#ffffff"
plt.rcParams["font.size"] = 11

# Data
books = pd.DataFrame({
    "BookID": range(1, 21),
    "Title": [
        "A Game of Thrones", "The Da Vinci Code", "The Hunger Games", "Life of Pi", "The Silent Patient",
        "Becoming", "Educated", "The Shining", "The Lord of the Rings", "The Midnight Library",
        "Gone Girl", "The Subtle Art of Not Giving a F*ck", "Sapiens: A Brief History of Humankind",
        "The Power of Now", "The Book Thief", "Thinking, Fast and Slow", "The Girl on the Train",
        "Atomic Habits", "The Seven Husbands of Evelyn Hugo", "The Name of the Wind"
    ],
    "Author": [
        "George R.R. Martin", "Dan Brown", "Suzanne Collins", "Yann Martel", "Alex Michaelides",
        "Michelle Obama", "Tara Westover", "Stephen King", "J.R.R. Tolkien", "Matt Haig",
        "Gillian Flynn", "Mark Manson", "Yuval Noah Harari", "Eckhart Tolle", "Markus Zusak",
        "Daniel Kahneman", "Paula Hawkins", "James Clear", "Taylor Jenkins Reid", "Patrick Rothfuss"
    ],
    "Genre": [
        "Fantasy", "Thriller", "Dystopian", "Adventure", "Psychological Thriller",
        "Autobiography", "Memoir", "Horror", "Fantasy", "Fiction",
        "Thriller", "Self-help", "History", "Spirituality", "Historical Fiction",
        "Psychology", "Thriller", "Self-help", "Romance", "Fantasy"
    ],
    "Copies": [5, 4, 6, 6, 5, 3, 2, 3, 7, 4, 5, 5, 3, 3, 6, 2, 3, 8, 4, 5]
})
members = pd.DataFrame({
    "MemberID": range(1, 21),
    "Name": [
        "Gaganpreet","Manmeet","Kavneet","Amrit","Eva","Jass","Harman","Harleen","Isha","Jaya",
        "Karan","Prabhjot","vansh","Ruby","Om","Priya","Samar","Naman","Taran","Sifat"
    ],
    "JoinDate": pd.date_range(start="2023-01-01", periods=20, freq='20D')
})

transactions = []
for _ in range(80):
    mem = int(random.choice(members["MemberID"]))
    book = int(random.choice(books["BookID"]))
    issue = datetime(2024, random.randint(1,12), random.randint(1,28))
    if random.random() < 0.85:
        ret = issue + timedelta(days=random.randint(3,28))
    else:
        ret = pd.NaT
    transactions.append({"MemberID": mem, "BookID": book, "IssueDate": issue, "ReturnDate": ret})
transactions = pd.DataFrame(transactions)

# Luxury theme colors
gold = "#D4AF37"
dark_gold = "#B68D2A"
black = "#121212"
emerald = "#0B5345"
royal_blue = "#0E4D92"
wine_red = "#6A0D2C"
cream = "#FDF5E6"
accent = gold

# KPI Cards
def kpi_cards(total_books, total_members, issued_now, overdue):
    html = f"""
    <div style="display:flex; gap:18px; font-family:Segoe UI, sans-serif; margin-bottom:12px;">
      <div style="background:linear-gradient(135deg,{gold},{dark_gold}); padding:18px; border-radius:12px; width:220px;">
        <div style="font-size:12px; color:{cream}">📚 Total Books</div>
        <div style="font-size:22px; font-weight:700; color:{cream}">{total_books}</div>
      </div>
      <div style="background:linear-gradient(135deg,{wine_red},{black}); padding:18px; border-radius:12px; width:220px;">
        <div style="font-size:12px; color:{cream}">👥 Total Members</div>
        <div style="font-size:22px; font-weight:700; color:{cream}">{total_members}</div>
      </div>
      <div style="background:linear-gradient(135deg,{emerald},{black}); padding:18px; border-radius:12px; width:220px;">
        <div style="font-size:12px; color:{cream}">📖 Currently Issued</div>
        <div style="font-size:22px; font-weight:700; color:{cream}">{issued_now}</div>
      </div>
      <div style="background:linear-gradient(135deg,{royal_blue},{black}); padding:18px; border-radius:12px; width:220px;">
        <div style="font-size:12px; color:{cream}">⏰ Overdue</div>
        <div style="font-size:22px; font-weight:700; color:{cream}">{overdue}</div>
      </div>
    </div>
    """
    display(HTML(html))

# Styled Table
def styled_table(df, max_rows=10):
    return (
        df.head(max_rows)
        .style.set_table_styles([
            {'selector': 'th', 'props': [('background-color', black), ('color', gold), ('font-weight', '700')]},
            {'selector': 'td', 'props': [('padding', '8px'), ('color', '#333')]},
        ])
    )

# Metrics
def compute_metrics():
    total_books = books["Copies"].sum()
    total_members = members.shape[0]
    issued_now = transactions[transactions["ReturnDate"].isna()].shape[0]
    cutoff = pd.Timestamp.now() - pd.Timedelta(days=21)
    overdue = transactions[(transactions["ReturnDate"].isna()) & (transactions["IssueDate"] < cutoff)].shape[0]
    return total_books, total_members, issued_now, overdue

# Charts
def books_by_genre_chart():
    genre_counts = books["Genre"].value_counts().reset_index()
    genre_counts.columns = ["Genre", "Count"]

    # Luxury colors (deep, elegant tones)
    luxury_colors = [
        "#0F52BA",  # Royal Blue
        "#800020",  # Burgundy
        "#FFD700",  # Gold
        "#2E8B57",  # Emerald Green
        "#4B0082",  # Indigo
        "#8B4513",  # Saddle Brown
        "#C0C0C0",  # Silver
        "#191970",  # Midnight Blue
        "#DAA520"   # Goldenrod
    ] * 3  # Repeat to handle many genres

    plt.figure(figsize=(8, 4.2))
    sns.barplot(data=genre_counts, x="Count", y="Genre", hue="Genre", palette=luxury_colors[:len(genre_counts)], legend=False)
    plt.title("Books by Genre", fontsize=14, weight='bold')
    plt.xlabel("Number of Copies")
    plt.tight_layout()
    plt.show()


def top_borrowed_chart(n=7):
    top = transactions["BookID"].value_counts().head(n).reset_index()
    top.columns = ["BookID", "Borrows"]
    top = top.merge(books[["BookID", "Title"]], on="BookID", how="left")

    # Luxury color palette
    luxury_colors = [
        "#0F52BA",  # Royal Blue
        "#800020",  # Burgundy
        "#FFD700",  # Gold
        "#2E8B57",  # Emerald Green
        "#4B0082",  # Indigo
        "#8B4513",  # Saddle Brown
        "#C0C0C0"   # Silver
    ][:len(top)]

    plt.figure(figsize=(8, 4.2))
    sns.barplot(data=top, x="Borrows", y="Title", hue="Title", palette=luxury_colors, legend=False)
    plt.title("Top Borrowed Books", fontsize=14, weight='bold')
    plt.tight_layout()
    plt.show()

def monthly_trend_chart():
    df = transactions.copy()
    df["Month"] = df["IssueDate"].dt.to_period("M").dt.to_timestamp()
    monthly = df.groupby("Month").size()

    royal_blue = "#0F52BA"  # Royal Blue

    plt.figure(figsize=(9, 3.2))
    plt.plot(monthly.index, monthly.values, marker='o', linewidth=2, color=royal_blue)
    plt.fill_between(monthly.index, monthly.values, alpha=0.18, color=royal_blue)
    plt.title("Monthly Borrowing Trend", fontsize=13, weight='bold')
    plt.ylabel("Number of Issues")
    plt.tight_layout()
    plt.show()


def top_readers_chart(n=5):
    top = transactions.groupby("MemberID").size().sort_values(ascending=False).head(n).reset_index()
    top.columns = ["MemberID","Borrows"]
    top = top.merge(members, on="MemberID", how="left")

    # Luxury colors
    luxury_colors = ["#D4AF37",  # Gold
                     "#000000",  # Black
                     "#0F52BA",  # Royal Blue
                     "#50C878",  # Emerald Green
                     "#800020"]  # Burgundy / Wine Red

    colors = sns.color_palette(luxury_colors[:len(top)])

    plt.figure(figsize=(7,3))
    sns.barplot(data=top, x="Borrows", y="Name", hue="Name", palette=colors, legend=False)
    plt.title("Top Readers", fontsize=13, weight='bold')
    plt.tight_layout()
    plt.show()


# Dashboard
def search_books(keyword):
    kw = str(keyword).lower()
    out = books[books["Title"].str.lower().str.contains(kw) | books["Author"].str.lower().str.contains(kw) | books["Genre"].str.lower().str.contains(kw)]
    if out.empty:
        print("No results found.")
    else:
        display(styled_table(out, max_rows=20))

def show_dashboard():
    clear_output(wait=True)
    tb, tm, issued, overdue = compute_metrics()
    kpi_cards(tb, tm, issued, overdue)
    print("\nTop 7 Borrowed Books:")
    top_b = transactions["BookID"].value_counts().head(7).reset_index()
    top_b.columns = ["BookID","Borrows"]
    top_b = top_b.merge(books[["BookID","Title"]], on="BookID")
    display(styled_table(top_b[["Title","Borrows"]], max_rows=7))
    books_by_genre_chart()
    top_borrowed_chart(7)
    monthly_trend_chart()
    top_readers_chart(5)

# Book/Member Management
def view_books():
    display(styled_table(books, max_rows=20))

def add_book():
    global books
    clear_output()
    print("➕ Add a new book")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    genre = input("Genre: ").strip() or "General"
    copies = int(input("Copies: ") or 1)
    new_id = int(books["BookID"].max()) + 1
    books.loc[len(books)] = [new_id, title, author, genre, copies]
    print("✅ Added. Returning to dashboard...")

def remove_book():
    global books
    clear_output()
    print("🗑️ Remove a book")
    bid = int(input("BookID to remove: "))
    books.drop(books[books["BookID"] == bid].index, inplace=True)
    print("Removed. Returning to dashboard...")

def view_members():
    display(styled_table(members, max_rows=50))

def add_member():
    global members
    clear_output()
    name = input("Member Name: ").strip()
    new_id = int(members["MemberID"].max()) + 1
    members.loc[len(members)] = [new_id, name, pd.Timestamp.now()]
    print("✅ Member added. Returning to dashboard...")

def issue_book():
    global books, transactions, members
    clear_output()
    print("Issue book to member")

    # Get member name and book title
    member_name = input("Member Name: ").strip()
    book_title = input("Book Title: ").strip()

    # Find corresponding IDs
    member_row = members[members["Name"].str.lower() == member_name.lower()]
    book_row = books[books["Title"].str.lower() == book_title.lower()]

    if member_row.empty:
        print("⚠️ Member not found.")
        return
    if book_row.empty:
        print("⚠️ Book not found.")
        return

    mid = member_row.iloc[0]["MemberID"]
    bid = book_row.iloc[0]["BookID"]

    # Check availability
    avail = books.loc[books["BookID"] == bid, "Copies"].sum()
    if avail > 0:
        books.loc[books["BookID"] == bid, "Copies"] -= 1
        transactions.loc[len(transactions)] = [mid, bid, pd.Timestamp.now(), pd.NaT]
        print("✅ Issued successfully!")
    else:
        print("❌ No copies available.")


def return_book():
    global books, transactions, members
    clear_output()
    print("Return book")

    # Get member name and book title instead of IDs
    member_name = input("Member Name: ").strip()
    book_title = input("Book Title: ").strip()

    # Find the corresponding IDs
    member_row = members[members["Name"].str.lower() == member_name.lower()]
    book_row = books[books["Title"].str.lower() == book_title.lower()]

    if member_row.empty:
        print("⚠️ Member not found.")
        return
    if book_row.empty:
        print("⚠️ Book not found.")
        return

    mid = member_row.iloc[0]["MemberID"]
    bid = book_row.iloc[0]["BookID"]

    # Find the issued record
    idx = transactions[
        (transactions["MemberID"] == mid) &
        (transactions["BookID"] == bid) &
        (transactions["ReturnDate"].isna())
    ].index

    if len(idx) > 0:
        transactions.loc[idx, "ReturnDate"] = pd.Timestamp.now()
        books.loc[books["BookID"] == bid, "Copies"] += 1
        print("✅ Returned. Thank you!")
    else:
        print("⚠️ No matching issued record found.")

# Menu
def menu():
    while True:
        print("\n===== 🌸 Pastel Library Management =====")
        print("1️⃣  View Dashboard")
        print("2️⃣  View Books")
        print("3️⃣  Add Book")
        print("4️⃣  Remove Book")
        print("5️⃣  View Members")
        print("6️⃣  Add Member")
        print("7️⃣  Issue Book")
        print("8️⃣  Return Book")
        print("9️⃣  Search Books")
        print("0️⃣  Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            show_dashboard()
        elif choice == '2':
            clear_output()
            view_books()
        elif choice == '3':
            add_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            clear_output()
            view_members()
        elif choice == '6':
            add_member()
        elif choice == '7':
            issue_book()
        elif choice == '8':
            return_book()
        elif choice == '9':
            q = input('Search keyword (title/author/genre): ').strip()
            clear_output()
            search_books(q)
        elif choice == '0':
            print('👋 Bbye!')
            break
        else:
            print('⚠️ Invalid choice. Try again.')

# Run Menu
menu()



