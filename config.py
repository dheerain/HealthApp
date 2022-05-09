#Remove Fiber Column and its references Protien Carbs Fat Calories Sequence
#Add Snack 1-2
#Total Of All Vertically

food_config = {
    'EGG': {'Protein': 6, 'Fat': 5,  'Carbs': 0, 'Calories': 69, 'Fiber': 1},
    'EGG WHITE': {'Protein': 3, 'Fat': 0,  'Carbs': 0, 'Calories': 12, 'Fiber': 1},
    'CHICKEN BREAST,FISH': {'Protein': .26, 'Fat': .04,  'Carbs': 0, 'Calories': 1.4, 'Fiber': 1},
   	'PANEER': {'Protein': .18, 'Fat': .22,  'Carbs': .03, 'Calories': 2.82, 'Fiber': 1},
   	'TOFU': {'Protein': .08, 'Fat': .05,  'Carbs': .02, 'Calories': .85, 'Fiber': 1},
   	'WHEY': {'Protein': 26, 'Fat': .5,  'Carbs': 3, 'Calories': 120, 'Fiber': 1},
    'SOYA CHUNKS': {'Protein': .525, 'Fat': .005,  'Carbs': .33, 'Calories': 3.465, 'Fiber': 1},
    'LENTILS,PULSES,LEGUMES': {'Protein': .25, 'Fat': .01,  'Carbs': .59, 'Calories': 3.45, 'Fiber': 1},
   	'MILK': {'Protein': .033, 'Fat': .021,  'Carbs': .05, 'Calories': .521, 'Fiber': 1},
   	'VEGGIES': {'Protein': .01, 'Fat': 0,  'Carbs': .08, 'Calories': .36, 'Fiber': 1},
   	'OIL,BUTTER,GHEE': {'Protein': 0, 'Fat': 1,  'Carbs': 0, 'Calories': 9, 'Fiber': 1},
    'BREAD': {'Protein': 3, 'Fat': 1,  'Carbs': 15, 'Calories': 81, 'Fiber': 1},
    'GRAINS': {'Protein': .1, 'Fat': 0,  'Carbs': .8, 'Calories': 3.6, 'Fiber': 1},
   	'FRUITS': {'Protein': 0, 'Fat': 0,  'Carbs': .22, 'Calories': .88, 'Fiber': 1},
   	'SUGAR,HONEY,JAGGERY': {'Protein': 0, 'Fat': 0,  'Carbs': 1, 'Calories': 4, 'Fiber': 1},
   	'DRY FRUITS': {'Protein': .16, 'Fat': .64,  'Carbs': .11, 'Calories': 6.84, 'Fiber': 1},
    'SEEDS': {'Protein': .2, 'Fat': .4,  'Carbs': .3, 'Calories': 5.6, 'Fiber': 1},
    'CHICKEN WHOLE': {'Protein': .24, 'Fat': .13,  'Carbs': 0, 'Calories': 2.13, 'Fiber': 1},
}


general_instruction = ["TAKE OMEGA 3 AND MULTIVITAMIN CAPSULE AFTER MEAL PREFERABLY AFTER BREAKFAST.",
                       "HAVE GOOD SLEEP ATLEAST 7-8 HOURS PER DAY.",
                       "CONSUME ATLEAST 4-5 LITER WATER PER DAY.",
                       "STAY ACTIVE THROUGHOUT THE DAY.",
                       "MEASURE THE FOOD IN RAW.",
                       "TAKE VITAMIN C  ONCE A DAY"]

disease_config = {
    'BP': [" PREFEBERLY USE SENDHA SALT INSTEAD OF NORMAL SALT.","DAILY RECOMANDED SALT INTAKE 1.5 GM PER DAY."],
    'PCOD,PCOS': ["IN OIL USE EXTRA VIRGIN OLIVE OIL PREFERABLY.",
                           "IN VEGETABLES CONSUME  CARROT, BROCOLLI, CAULIFLOWER, SPINICH, CAPCICUM, MUSHROOM, LADY FINGER, CUCUMBER, ONION, TOMATO, CORRIENDER, GHIA, TINDA, BAINGAN, KERELA,PEAS,GARLIC,GINGER PREFEREABLY.",
                           "IN GRAINS CONSUME OATS, BARLEY,CHANA ATTA,BROWN RICE, PREFERABLY.,IN FRUITS APPLE, BANANA, ORANGE PREFERABLY.",
                           "IN PULSES USE KIDNEY BEANS,CHICK PEAS AND LENTILS PREFERABLY.", "AVOID THESE FOOD ITEMS-PAPAYA, PINEAPPLE,GRAPES AND MELON,POTATOES,WHITE BREAD,COOKIES,PASTA AND MAGGIE,MAIDA,SWEETS AND REFINED SUGAR, JAGGERY,COFFEE"],
    'DIABETIES': ["INCREASE MEAL FREQUENCY.","DO WORKOUT AFTER HAVING SOME MEAL.","EAT 1 GARLIC CLOVE BEFORE MEAL."],
    'THYROID': [" USE IODIZED SALT.","CRUCIFEROUS VEGETABLES  (CABBAGE, CAULIFLOWER, BROCOLLI, TURNIP, RADISH ETC.) AND SOYA CHUNKS ARE WELL COOKED BEFORE CONSUMING."]
}


