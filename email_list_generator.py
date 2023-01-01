
def add_arbitrary_numbers(name_pair):
    possible_combinations = [f"{name_pair[0]}{name_pair[1]}"]

    #cover smaller numbers like sports numbers and abbreviated years
    for i in range(0,100):
        possible_combinations.append(f"{name_pair[0]}.{name_pair[1]}{i}")
        possible_combinations.append(f"{name_pair[0]}{name_pair[1]}{i}")
    
    #cover from 1950-2050 for birth years and grad years
    for i in range(1950, 2050):
        possible_combinations.append(f"{name_pair[0]}.{name_pair[1]}{i}")
        possible_combinations.append(f"{name_pair[0]}{name_pair[1]}{i}")

    return possible_combinations

def main():
    first_names = ["james", "robert", "michael", "david", "william", "richard", 
        "dick", "joseph", "joe", "thomas", "tom", "charles", "chuck", "christopher", "chris",
        "matthew", "matt", "anthony", "tony", "mark", "donald", "don", "steven", "steve", "paul",
        "andrew", "drew", "joshua", "josh", "kenneth", "ken", "kenny", "kevin", "brian", "george",
        "timothy", "tim", "ronald", "ron", "edward", "ed", "jason", "jeffrey", "jeff", "ryan", "jacob", "jake",
        "gary", "nicholas", "nick", "eric", "erik", "jonathan", "jon", "john", "stephen", "larry", "justin", "scott",
        "brandon", "benjamin", "ben", "samuel", "sam", "gregory", "greg", "alexander", "alex", "frank", "patrick", "rick",
        "raymond", "ray", "jack", "jackson", "dennis", "jerry", "tyler", "aaron", "jose", "adam", "nathan", "nate", "henry",
        "douglas", "doug", "zachary", "zach", "zack", "peter", "pete", "kyle", "ethan", "walter", "noah", "jeremy",
        "christian", "keith", "roger", "terry", "gerald", "harold", "sean", "shawn", "austin", "carl", "arthur",
        "lawrence", "dylan", "jesse", "jesse", "jordan", "bryan", "billy", "bruce", "gabriel", "gabe", "logan",
        "albert", "al", "willie", "willy", "alan", "juan", "wayne", "elijah", "eli", "randy", "roy", "vincent", "vince",
        "ralph", "eugene", "russell", "russ", "bobby", "mason", "philip", "phil", "phillip", "louis", "lou", "louie", "lewis",
        "logan", "devin", "dorian",
        "mary", "patricia", "pat", "pattie", "jennifer", "jenny", "jen", "linda", "elizabeth", "liz", "beth", "barbara", "barb",
        "susan", "sue", "jessica", "jess", "sarah", "sara", "karen", "lisa", "nancy", "betty", "margaret", "sandra", "ashley",
        "kimberly", "emily", "donna", "michelle", "carol", "amanda", "dorothy", "melissa", "deborah", "stephanie", "rebecca",
        "sharon", "laura", "cynthia", "kathleen", "amy", "angela", "shirley", "anna", "brenda", "pamela", "emma", "nicole",
        "helen", "samantha", "sam", "katherine", "kat", "christine", "debra", "rachel", "carolyn", "janet", "catherine",
        "maria", "heather", "diane", "ruth", "julie", "olivia", "joyce", "virginia", "victoria", "kelly", "lauren",
        "christina", "joan", "evelyn", "judith", "megan", "andrea", "cheryl", "hannah", "jacqueline", "jackie", "martha",
        "gloria", "teresa", "ann", "anne", "madison", "frances", "kathryn", "janice", "jean", "abigail", "abby",
        "alice", "julia", "judy", "sophia", "sophie", "grace", "denise", "amber", "doris", "marilyn", "danielle",
        "beverly", "bev", "isabelle", "belle", "theresa", "diana", "natalie", "brittany", "charlotte", "marie",
        "kayla", "alexis", "lori"] #https://www.ssa.gov/oact/babynames/decades/century.html
    
    last_names = ["wang", "smith", "devi", "ivanov", "kim", "ali", "garcia", "muller", "silva", "dasilva", "mohammed",
        "tesfaye", "nguyen", "ilunga", "gonzalez", "deng", "rodriguez", "moyo", "hansen", "zhang", "johnson", "williams",
        "brown", "jones", "anderson", "hernandez", "lopez", "miller", "chavez", "davis", "wilson", "thomas", "taylor",
        "moore", "jackson", "martin", "lee", "perez", "thompson", "white", "haris", "sanchez", "clark", "ramirez",
        "lewis", "robinson", "walker", "young", "allen", "king", "right", "scott", "torres", "hill", "flores", "green",
        "adams", "nelson", "baker", "hall", "rivera", "campbell", "mitchell", "carter", "roberts", "gomez", "phillips",
        "evans", "turner", "diaz", "parker", "cruz", "edwards", "collins", "reyes", "stewart", "morris", "morales",
        "murphy", "cook", "rogers", "gutierrez", "ortiz", "morgan", "cooper", "peterson", "bailey", "reed", "kelly",
        "howard", "ramos", "kim", "cox", "ward", "richardson", "watson", "brooks", "chavez", "wood", "james",
        "bennet", "grey", "mendoza", "ruiz", "hughes", "price", "alvarez", "catillo", "sanders", "patel", "myers", 
        "ross", "foster", "jimenez"] #https://www.thoughtco.com/most-common-us-surnames-1422656
    email_hosts = ["gmail.com", "outlook.com", "hotmail.com"]

    all_possible_names = [(a, b) for a in first_names for b in last_names]

    with open("generated_emails.txt", "w") as f:
        for names in all_possible_names:
            bastardized_names = add_arbitrary_numbers(names)

            for name in bastardized_names:
                for host in email_hosts:
                    f.write(f"{name}@{host}\n")

if __name__ == "__main__":
    main()