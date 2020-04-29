# CREATE AN ART MARKETPLACE
# Veneer
# Here at Veneer we strive to provide the best marketplace experience to connect
# vetted art dealers with premium galleries. Create a marketplace for people and
# organizations to buy and sell pieces of art!
#
# In this project we’ll be developing classes and objects that represent the
# various responsibilities of art dealership software.

# --- Define classes

class Art:
    def __init__(self, artist, title, medium, year, owner):
        # Assign self properties to the arguments passed
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return '{artist}. \"{title}\". {year}, {medium}. {owner}, {location}'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)

class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing) # Append a new instance of the class Listing

    def remove_listing(self, del_listing):
        self.listings.remove(del_listing) # Remove the instance of the Listing class

    def show_listings(self):
        for listing in self.listings:
            print(listing)

class Client:
    def __init__(self, name, location, is_museum, wishlist=[]):
        self.name = name
        self.is_museum = is_museum
        self.wishlist = wishlist
        if is_museum: # Check if the Client is a museum
            self.location = location
        else:
            self.location = 'Private Collection'

    def sell_artwork(self, artwork, price):
        if artwork.owner == self: # Check that the Client can sell this artwork
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self: # Check that the Client doesn't own the artwork already
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)

    def add_wishlist(self, artwork):
        if artwork.owner != self: # Check that the Client doesn't own the artwork already
            self.wishlist.append(artwork)
            return '%s added to the wishlist!' % (artwork)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '%s, %s.' % (self.art.title, self.price)

# --- Build Marketplaces

veneer = Marketplace()

# --- Build Clients

edytta = Client('Edytta Halpirt', None, False)
moma = Client('MOMA', 'New York', True)

# --- Create some artwork

girl_with_mandolin = Art(
    'Picasso, Pablo',
    'Girl with a Mandolin (Fanny Tellier)',
    'oil on canvas',
    1910,
    edytta
    )
#print(girl_with_mandolin) # check the artwork created

edytta.sell_artwork(girl_with_mandolin, '$6M (USD)') # Put artwork up for sale

veneer.show_listings() # Check current artwork available at the marketplace

moma.buy_artwork(girl_with_mandolin) # Buy a certain piece of artwork
print(girl_with_mandolin) # Check if the artwork's owner was updated successfully
veneer.show_listings()
