
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
    first_names = ["james", "robert", "michael", "david"] #https://www.ssa.gov/oact/babynames/decades/century.html
    last_names = ["wang", "smith", "devi", "ivanov", "kim", "ali", "garcia", "muller", "silva", "dasilva"] #https://www.babbel.com/en/magazine/most-common-last-names-around-the-world
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