"""Grade 4 Math · Unit 1: Place Value, Rounding, and Whole Numbers (Oct 12 – Nov 6, 2026)."""
from engine import Unit
from content.math4.unit01_a import LESSONS_A, CHECKS_A
from content.math4.unit01_b import LESSONS_B, CHECKS_B, REVIEW, TEST

LESSONS = LESSONS_A + LESSONS_B

UNIT = Unit(
    1, "Place Value, Rounding, and Whole Numbers",
    "How our number system works, and how to read, compare, round, add, and subtract numbers up to one million.",
    "Every number you will work with this year is built from place value. In this unit you will see how each place is worth "
    "ten times the place to its right, read and write numbers up to one million, compare and order them, round them to "
    "friendly numbers, and add and subtract them with the standard algorithm.",
    ["Explain why each place is worth 10 times the place to its right.",
     "Read and write numbers to 1,000,000 in standard, word, and expanded form.",
     "Compare and order multi-digit numbers using >, =, and <.",
     "Round numbers to any place and use rounding to estimate.",
     "Add and subtract multi-digit numbers with the standard algorithm and check if answers are reasonable."],
    [("4.NBT.1", "Recognize that in a multi-digit whole number, a digit in one place represents ten times what it represents in the place to its right."),
     ("4.NBT.2", "Read and write multi-digit whole numbers using base-ten numerals, number names, and expanded form. Compare two multi-digit numbers using >, =, and <."),
     ("4.NBT.3", "Use place value understanding to round multi-digit whole numbers to any place."),
     ("4.NBT.4", "Fluently add and subtract multi-digit whole numbers using the standard algorithm."),
     ("4.OA.3", "Solve multistep word problems; assess the reasonableness of answers using mental computation and estimation strategies including rounding.")],
    [("place value", "The value a digit has because of its place in a number."),
     ("period", "A group of three places separated by a comma."),
     ("expanded form", "A number written as the sum of the values of its digits."),
     ("round", "To change a number to a nearby friendly number."),
     ("estimate", "A close answer found with rounded numbers."),
     ("regroup", "To trade 10 of one unit for 1 of the next bigger unit, or the reverse.")],
    ["Read, write, and compare numbers to 1,000 (Grade 3).", "Round to the nearest 10 or 100 (Grade 3).",
     "Add and subtract within 1,000 with regrouping (Grade 3).", "Addition and subtraction facts to 20 from memory."],
    ["Base-ten blocks (or paper cut-outs of cubes, flats, rods, and units)", "Place-value chart (six places) in a sheet protector and a dry-erase marker",
     "Play money: $1, $10, $100, and $1,000 bills", "Painter's tape or a long paper strip for a floor number line", "Grid paper", "Digit cards 0–9 (two sets)"],
    LESSONS, CHECKS_A + CHECKS_B, REVIEW, TEST,
    real_world="Big numbers are everywhere: the number of people in Mississippi (about 2.9 million), the miles on a car, the price of a house, "
               "or the seats in a stadium. Place value helps you read them, and rounding helps you talk about them quickly.",
    family_note="Keep the place-value chart and money handy all unit. Ask your child to read big numbers they see in daily life "
                "(gas prices, mileage, store totals) and to round them. A few minutes of this each day builds strong number sense.",
    weeks=[("Week 1 · Oct 12–16", [("Mon 10/12", "1.1", "How Place Value Works"), ("Tue 10/13", "1.2", "Place Value to One Million"),
                                   ("Wed 10/14", "1.3", "The Value of a Digit"), ("Thu 10/15", "1.4", "Standard, Word, and Expanded Form"),
                                   ("Fri 10/16", "Check", "Weekly Check 1")]),
           ("Week 2 · Oct 19–23", [("Mon 10/19", "1.5", "Renaming Numbers"), ("Tue 10/20", "1.6", "Comparing Multi-Digit Numbers"),
                                   ("Wed 10/21", "1.7", "Ordering Numbers"), ("Thu 10/22", "1.8", "Large Numbers on a Number Line"),
                                   ("Fri 10/23", "Check", "Weekly Check 2")]),
           ("Week 3 · Oct 26–30", [("Mon 10/26", "1.9", "Rounding with a Number Line"), ("Tue 10/27", "1.10", "Rounding to Any Place"),
                                   ("Wed 10/28", "1.11", "Estimating Sums and Differences"), ("Thu 10/29", "1.12", "Is My Answer Reasonable?"),
                                   ("Fri 10/30", "Check", "Weekly Check 3")]),
           ("Week 4 · Nov 2–6", [("Mon 11/2", "1.13", "Adding Multi-Digit Numbers"), ("Tue 11/3", "1.14", "Subtracting with Regrouping"),
                                 ("Wed 11/4", "1.15", "Subtracting Across Zeros"), ("Thu 11/5", "1.16", "Solving Multi-Step Word Problems + Unit Review"),
                                 ("Fri 11/6", "Test", "Unit 1 Test")])])
