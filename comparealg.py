import csv
#compare lines
print('Here are some lines to check out:')
with open('nba-player-props-rotowire.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        sites = []

        #sets each line according to the column of the csv
        name = line[0]
        if line[3]:
            points_bet = float(line[3])
            sites.append('PointsBet')
        else: 
            points_bet = None
        if line[6]:
            draft_kings = float(line[6])
            sites.append('DraftKings')
        else: 
            draft_kings = None
        if line[9]:
            fanduel = float(line[9])
            sites.append('FanDuel')
        else: 
            fanduel = None
        if line[12]:
            betmgm = float(line[12])
            sites.append('BetMGM')
        else: 
            betmgm = None
        site_lines = [points_bet, draft_kings, fanduel, betmgm]
        num_lines = 0
        for line in site_lines:
            if line:
                num_lines+=1
        # if num_lines == 1:
        #     print(f'For {name}, there is only one line.')
        # else:
        new_site_lines = [line for line in site_lines if line]
        average_line = (sum(new_site_lines)) / (len(new_site_lines))
        #greatest_discrepancy = max(map(abs, [points_bet - average_line, draft_kings-average_line, fanduel-average_line, betmgm-average_line]))
        discrepancies = [abs((new_site_lines[i] - average_line)) for i in range(len(new_site_lines))]
        greatest_discrepancy = max(discrepancies)
        index = discrepancies.index(greatest_discrepancy)
        if greatest_discrepancy == 0:
            print(f'For {name}, all lines are the same.')
        else:
            print(f'For {name}, the line with the greatest difference from the average line is from {sites[index]}. That difference is {greatest_discrepancy}')
        
        if greatest_discrepancy >= 1:
             print(f'For {name}, the line with the greatest difference from the average line is from {sites[index]}. That difference is {greatest_discrepancy}')

    #print('For Patrick Beverly, the line with the greatest difference from the average line is from Sleeper. That difference is 1. The category is blocks.')