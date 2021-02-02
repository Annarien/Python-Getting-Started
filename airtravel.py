""" Following the course work from Core Python: Getting Started
 @ https://app.pluralsight.com/course-player?clipId=6a8cd449-5cc9-4b28-b52c-507a8fac7aa2

 Model for aircraft flights."""


class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        # this checks to see if the first two characters  in a flight name is letters;
        # if the first two characters are not numbers, then a ValueError is raised.
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        # now we check to see if the first two characters are uppercase, and raise a ValueError if it is not.
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        # check to see if the remaining four characters are digits and is between 0 and 9999,
        # raising a ValueError if it is not.
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number  # _number is used to avoid a name clash with the number() function
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    # getting airline code
    def airline(self):
        return self._number[:2]  # saving first 2 characters which represents airline code

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat:       A seat designator such a '12C' or '21F'.
            passenger:  The passenger name.

        Raises:
            ValueError: If the seat is unavailable
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat:  The existing seat designator for the passenger to be moved.
            to_seat:    The new seat designator
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_card(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):


    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Aircraft: {aircraft}" \
             " |"

    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Rich Hickey")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("55K", "Larry Wall")
    g.allocate_seat("33G", "Yukihiro Matsumoto")
    g.allocate_seat("4B", "Brian Kernighan")
    g.allocate_seat("4A", "Dennis Ritchie")

    return f, g
