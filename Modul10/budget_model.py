class Model:
    def __init__(self, connection):
        self.connection = connection

    def init_db(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            create table if not exists BUD_CATEGORIES (id integer primary key, category_name text)
        ''')

        cursor.execute('''
            create table if not exists BUD_ITEMS (
                id integer primary key,
                name text,
                category_id integer,
                amount real,
                date date,
            foreign key (category_id) references BUD_CATEGORIES(id))
        ''')

    def get_or_create_category(self, name):
        cursor = self.connection.cursor()
        cursor.execute('select id from BUD_CATEGORIES where category_name=?', (name,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute('insert into BUD_CATEGORIES values(null, ?)', (name,))
            self.connection.commit()
            category_id = cursor.lastrowid
        else:
            category_id = result[0]

        return category_id

    def add_item(self, name, category, amount, date):
        category_id = self.get_or_create_category(category)
        cursor = self.connection.cursor()
        cursor.execute('insert into BUD_ITEMS values(null, ?, ?, ?, ?)', (name, category_id, amount, date))
        self.connection.commit()

    def delete_item(self, item_id):
        cursor = self.connection.cursor()
        cursor.execute('delete from BUD_ITEMS where id=?', (item_id,))
        self.connection.commit()

    def list_items(self):
        cursor = self.connection.cursor()
        return cursor.execute('select * from BUD_ITEMS order by date')
