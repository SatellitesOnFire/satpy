"""Real world test data for GMS-5 VISSR unit tests."""

import numpy as np

import satpy.readers.gms5_vissr_l1b as vissr

ATTITUDE_PREDICTION = np.array(
    [
        (
            50130.93055556,
            (19960217, 222000),
            3.14911863,
            0.00054604,
            4.3324597,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.93402778,
            (19960217, 222500),
            3.14911863,
            0.00054604,
            4.31064812,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.9375,
            (19960217, 223000),
            3.14911863,
            0.00054604,
            4.28883633,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.94097222,
            (19960217, 223500),
            3.14911863,
            0.00054604,
            4.26702432,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.94444444,
            (19960217, 224000),
            3.14911863,
            0.00054604,
            4.2452121,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.94791667,
            (19960217, 224500),
            3.14911863,
            0.00054604,
            4.22339966,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.95138889,
            (19960217, 225000),
            3.14911863,
            0.00054604,
            4.201587,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.95486111,
            (19960217, 225500),
            3.14911863,
            0.00054604,
            4.17977411,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.95833333,
            (19960217, 230000),
            3.14911863,
            0.00054604,
            4.157961,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.96180556,
            (19960217, 230500),
            3.14911863,
            0.00054604,
            4.13614765,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.96527778,
            (19960217, 231000),
            3.14911863,
            0.00054604,
            4.11433408,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.96875,
            (19960217, 231500),
            3.14911863,
            0.00054604,
            4.09252027,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.97222222,
            (19960217, 232000),
            3.14911863,
            0.00054604,
            4.07070622,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.97569444,
            (19960217, 232500),
            3.14911863,
            0.00054604,
            4.04889193,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.97916667,
            (19960217, 233000),
            3.14911863,
            0.00054604,
            4.02707741,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.98263889,
            (19960217, 233500),
            3.14911863,
            0.00054604,
            4.00526265,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.98611111,
            (19960217, 234000),
            3.14911863,
            0.00054604,
            3.98344765,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.98958333,
            (19960217, 234500),
            3.14911863,
            0.00054604,
            3.96163241,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.99305556,
            (19960217, 235000),
            3.14911863,
            0.00054604,
            3.93981692,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50130.99652778,
            (19960217, 235500),
            3.14911863,
            0.00054604,
            3.9180012,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.0,
            (19960218, 0),
            3.14911863,
            0.00054604,
            3.89618523,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.00347222,
            (19960218, 500),
            3.14911863,
            0.00054604,
            3.87436903,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.00694444,
            (19960218, 1000),
            3.14911863,
            0.00054604,
            3.85255258,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.01041667,
            (19960218, 1500),
            3.14911863,
            0.00054604,
            3.8307359,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.01388889,
            (19960218, 2000),
            3.14911863,
            0.00054604,
            3.80891898,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.01736111,
            (19960218, 2500),
            3.14911863,
            0.00054604,
            3.78710182,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.02083333,
            (19960218, 3000),
            3.14911863,
            0.00054604,
            3.76528442,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.02430556,
            (19960218, 3500),
            3.14911863,
            0.00054604,
            3.74346679,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.02777778,
            (19960218, 4000),
            3.14911863,
            0.00054604,
            3.72164893,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.03125,
            (19960218, 4500),
            3.14911863,
            0.00054604,
            3.69983084,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.03472222,
            (19960218, 5000),
            3.14911863,
            0.00054604,
            3.67801252,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.03819444,
            (19960218, 5500),
            3.14911863,
            0.00054604,
            3.65619398,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
        (
            50131.04166667,
            (19960218, 10000),
            3.14911863,
            0.00054604,
            3.63437521,
            99.21774527,
            0.97415452,
            -1.56984055,
            0.0,
            0,
            0,
        ),
    ],
    dtype=vissr.ATTITUDE_PREDICTION_DATA,
)

ORBIT_PREDICTION_1 = np.array(
    [
        (
            50130.96180556,
            (960217, 230500),
            [2247604.14185506, -42110997.39399951, -276688.79765022],
            [3069.77904265, 164.12584895, 3.65437628],
            [-32392525.09983424, 27002204.93121811, -263873.25702763],
            [0.81859376, 0.6760037, 17.44588753],
            133.46391815,
            (330.12326803, -12.19424863),
            (197.27884747, -11.96904141),
            [
                [9.99936382e-01, 1.03449318e-02, 4.49611916e-03],
                [-1.03447475e-02, 9.99946490e-01, -6.42483646e-05],
                [-4.49654321e-03, 1.77330598e-05, 9.99989890e-01],
            ],
            [2.46885475e08, -2.07840219e08, -7.66028692e07],
            (-0.35887085, 140.18562594, 35793706.31768975),
            0,
            0,
        ),
        (
            50130.96527778,
            (960217, 231000),
            [3167927.33749398, -42051692.51095297, -275526.52514815],
            [3065.46435995, 231.22434208, 4.09379482],
            [-32392279.4626506, 27002405.27592725, -258576.96255205],
            [0.81939962, 0.66017389, 17.86159393],
            134.71734048,
            (330.12643276, -12.19310271),
            (196.02858456, -11.9678881),
            [
                [9.99936382e-01, 1.03449336e-02, 4.49611993e-03],
                [-1.03447493e-02, 9.99946490e-01, -6.42473793e-05],
                [-4.49654398e-03, 1.77320586e-05, 9.99989890e-01],
            ],
            [2.46204142e08, -2.07689897e08, -7.65268207e07],
            (-0.35166851, 140.18520316, 35793613.0815237),
            0,
            0,
        ),
        (
            50130.96875,
            (960217, 231500),
            [4086736.12968183, -41972273.80964861, -274232.7185828],
            [3059.68341675, 298.21262775, 4.53123515],
            [-32392033.65156128, 27002600.83510851, -253157.23498394],
            [0.81975174, 0.6441, 18.26873686],
            135.97076281,
            (330.12959087, -12.19195587),
            (194.77831505, -11.96673388),
            [
                [9.99936382e-01, 1.03449353e-02, 4.49612071e-03],
                [-1.03447510e-02, 9.99946490e-01, -6.42463940e-05],
                [-4.49654474e-03, 1.77310575e-05, 9.99989890e-01],
            ],
            [2.45524133e08, -2.07559497e08, -7.64508451e07],
            (-0.3442983, 140.18478523, 35793516.57370046),
            0,
            0,
        ),
        (
            50130.97222222,
            (960217, 232000),
            [5003591.03339227, -41872779.15809826, -272808.0027587],
            [3052.43895532, 365.05867777, 4.9664885],
            [-32391787.80234722, 27002791.53735474, -247616.67261456],
            [0.81965461, 0.62779672, 18.66712192],
            137.22418515,
            (330.13274246, -12.19080808),
            (193.52803902, -11.9655787),
            [
                [9.99936382e-01, 1.03449371e-02, 4.49612148e-03],
                [-1.03447528e-02, 9.99946490e-01, -6.42454089e-05],
                [-4.49654551e-03, 1.77300565e-05, 9.99989890e-01],
            ],
            [2.44845888e08, -2.07448982e08, -7.63749418e07],
            (-0.33676374, 140.18437233, 35793416.91561355),
            0,
            0,
        ),
        (
            50130.97569444,
            (960217, 232500),
            [5918053.49286455, -41753256.02295399, -271253.06495935],
            [3043.73441705, 431.73053079, 5.39934712],
            [-32391542.0492856, 27002977.3157848, -241957.93142027],
            [0.81911313, 0.61127876, 19.05655891],
            138.47760748,
            (330.13588763, -12.1896593),
            (192.27775657, -11.96442254),
            [
                [9.99936382e-01, 1.03449388e-02, 4.49612225e-03],
                [-1.03447545e-02, 9.99946490e-01, -6.42444238e-05],
                [-4.49654627e-03, 1.77290557e-05, 9.99989890e-01],
            ],
            [2.44169846e08, -2.07358303e08, -7.62991102e07],
            (-0.32906846, 140.18396465, 35793314.23041636),
            0,
            0,
        ),
        (
            50130.97916667,
            (960217, 233000),
            [6829686.08751574, -41613761.44760592, -269568.65462124],
            [3033.5739409, 498.19630731, 5.82960444],
            [-32391296.52466749, 27003158.10847847, -236183.72381214],
            [0.81813262, 0.59456087, 19.43686189],
            139.73102981,
            (330.1390265, -12.18850951),
            (191.02746783, -11.96326537),
            [
                [9.99936382e-01, 1.03449406e-02, 4.49612302e-03],
                [-1.03447563e-02, 9.99946490e-01, -6.42434389e-05],
                [-4.49654703e-03, 1.77280550e-05, 9.99989890e-01],
            ],
            [2.43496443e08, -2.07287406e08, -7.62233495e07],
            (-0.32121612, 140.18356238, 35793208.6428103),
            0,
            0,
        ),
        (
            50130.98263889,
            (960217, 233500),
            [7738052.74476409, -41454362.02480648, -267755.58296603],
            [3021.96236148, 564.42422513, 6.25705512],
            [-32391051.35918404, 27003333.85786499, -230296.81731314],
            [0.81671881, 0.57765777, 19.80784932],
            140.98445214,
            (330.14215916, -12.18735869),
            (189.77717289, -11.96210717),
            [
                [9.99936381e-01, 1.03449423e-02, 4.49612379e-03],
                [-1.03447580e-02, 9.99946489e-01, -6.42424541e-05],
                [-4.49654778e-03, 1.77270545e-05, 9.99989890e-01],
            ],
            [2.42826115e08, -2.07236222e08, -7.61476592e07],
            (-0.3132105, 140.18316567, 35793100.27882991),
            0,
            0,
        ),
        (
            50130.98611111,
            (960217, 234000),
            [8642718.9445816, -41275133.86582235, -265814.72261683],
            [3008.90520686, 630.38261431, 6.68149519],
            [-32390806.68247503, 27003504.50991426, -224300.03325666],
            [0.81487783, 0.56058415, 20.16934411],
            142.23787447,
            (330.14528573, -12.18620679),
            (188.52687186, -11.9609479),
            [
                [9.99936381e-01, 1.03449440e-02, 4.49612456e-03],
                [-1.03447598e-02, 9.99946489e-01, -6.42414694e-05],
                [-4.49654854e-03, 1.77260540e-05, 9.99989890e-01],
            ],
            [2.42159297e08, -2.07204676e08, -7.60720382e07],
            (-0.30505542, 140.18277471, 35792989.2656269),
            0,
            0,
        ),
        (
            50130.98958333,
            (960217, 234500),
            [9543251.93095296, -41076162.56379041, -263747.00717057],
            [2994.40869593, 696.03993248, 7.10272213],
            [-32390562.62077149, 27003670.01680953, -218196.24541058],
            [0.81261619, 0.54335463, 20.52117372],
            143.4912968,
            (330.14840632, -12.18505381),
            (187.27656486, -11.95978754),
            [
                [9.99936381e-01, 1.03449458e-02, 4.49612532e-03],
                [-1.03447615e-02, 9.99946489e-01, -6.42404848e-05],
                [-4.49654930e-03, 1.77250538e-05, 9.99989890e-01],
            ],
            [2.41496422e08, -2.07192684e08, -7.59964859e07],
            (-0.29675479, 140.18238966, 35792875.73125207),
            0,
            0,
        ),
    ],
    dtype=vissr.ORBIT_PREDICTION_DATA,
)

ORBIT_PREDICTION_2 = np.array(
    [
        (
            50130.99305556,
            (960217, 235000),
            [10439220.91492008, -40857543.15396438, -261553.43075696],
            [2978.47973561, 761.36477969, 7.52053495],
            [-32390319.30020279, 27003830.33282405, -211988.37862591],
            [0.80994076, 0.52598377, 20.86317023],
            144.74471913,
            (330.15152105, -12.1838997),
            (186.026252, -11.95862606),
            [
                [9.99936381e-01, 1.03449475e-02, 4.49612609e-03],
                [-1.03447632e-02, 9.99946489e-01, -6.42395003e-05],
                [-4.49655005e-03, 1.77240537e-05, 9.99989890e-01],
            ],
            [2.40837919e08, -2.07200148e08, -7.59210011e07],
            (-0.28831259, 140.18201066, 35792759.80443729),
            0,
            0,
        ),
        (
            50130.99652778,
            (960217, 235500),
            [11330197.2840407, -40619380.06793167, -259235.04755252],
            [2961.12591755, 826.32591367, 7.93473432],
            [-32390076.84311398, 27003985.41857829, -205679.40741202],
            [0.80685878, 0.50848599, 21.19517045],
            145.99814147,
            (330.15463004, -12.18274445),
            (184.77593341, -11.95746344),
            [
                [9.99936381e-01, 1.03449492e-02, 4.49612685e-03],
                [-1.03447650e-02, 9.99946489e-01, -6.42385159e-05],
                [-4.49655080e-03, 1.77230537e-05, 9.99989890e-01],
            ],
            [2.40184218e08, -2.07226967e08, -7.58455830e07],
            (-0.27973286, 140.18163787, 35792641.6143761),
            0,
            0,
        ),
        (
            50131.0,
            (960218, 0),
            [12215754.80493221, -40361787.08463053, -256792.97127933],
            [2942.35551459, 890.89226454, 8.34512262],
            [-32389835.37113104, 27004135.23720251, -199272.35452792],
            [0.8033778, 0.49087558, 21.51701595],
            147.2515638,
            (330.15773341, -12.18158803),
            (183.5256092, -11.95629965),
            [
                [9.99936381e-01, 1.03449510e-02, 4.49612761e-03],
                [-1.03447667e-02, 9.99946489e-01, -6.42375317e-05],
                [-4.49655155e-03, 1.77220539e-05, 9.99989890e-01],
            ],
            [2.39535744e08, -2.07273025e08, -7.57702305e07],
            (-0.2710197, 140.18127143, 35792521.29050537),
            0,
            0,
        ),
        (
            50131.00347222,
            (960218, 500),
            [13095469.82708225, -40084887.27645436, -254228.37467049],
            [2922.17747695, 955.03294974, 8.75150409],
            [-32389595.00191828, 27004279.7580633, -192770.28953487],
            [0.79950572, 0.47316669, 21.82855319],
            148.50498613,
            (330.16083128, -12.18043041),
            (182.27527951, -11.95513466),
            [
                [9.99936381e-01, 1.03449527e-02, 4.49612837e-03],
                [-1.03447684e-02, 9.99946489e-01, -6.42365476e-05],
                [-4.49655230e-03, 1.77210542e-05, 9.99989890e-01],
            ],
            [2.38892921e08, -2.07338200e08, -7.56949425e07],
            (-0.26217728, 140.18091148, 35792398.96228714),
            0,
            0,
        ),
        (
            50131.00694444,
            (960218, 1000),
            [13968921.48773305, -39788812.95011112, -251542.48890031],
            [2900.60142795, 1018.71728887, 9.15368488],
            [-32389355.85220329, 27004418.95297137, -186176.32730922],
            [0.79525074, 0.45537327, 22.12963356],
            149.75840846,
            (330.16392379, -12.17927157),
            (181.02494445, -11.95396845),
            [
                [9.99936381e-01, 1.03449544e-02, 4.49612913e-03],
                [-1.03447701e-02, 9.99946489e-01, -6.42355636e-05],
                [-4.49655305e-03, 1.77200547e-05, 9.99989890e-01],
            ],
            [2.38256170e08, -2.07422360e08, -7.56197178e07],
            (-0.25320985, 140.18055815, 35792274.75899146),
            0,
            0,
        ),
        (
            50131.01041667,
            (960218, 1500),
            [14835691.90970188, -39473705.58489136, -248736.60300345],
            [2877.63765957, 1081.9148182, 9.55147314],
            [-32389118.03536845, 27004552.79890675, -179493.62657611],
            [0.79062131, 0.43750908, 22.42011344],
            151.01183079,
            (330.16701107, -12.17811148),
            (179.77462147, -11.952801),
            [
                [9.99936381e-01, 1.03449561e-02, 4.49612989e-03],
                [-1.03447719e-02, 9.99946489e-01, -6.42345798e-05],
                [-4.49655380e-03, 1.77190553e-05, 9.99989890e-01],
            ],
            [2.37625908e08, -2.07525364e08, -7.55445552e07],
            (-0.24412169, 140.18021156, 35792148.80948149),
            0,
            0,
        ),
        (
            50131.01388889,
            (960218, 2000),
            [15695366.40490882, -39139715.76420763, -245812.06324505],
            [2853.29712752, 1144.59530548, 9.94467917],
            [-32388881.66227116, 27004681.27687033, -172725.38836895],
            [0.7856262, 0.41958762, 22.69985431],
            152.26525312,
            (330.17009324, -12.17695013),
            (178.52427609, -11.95163228),
            [
                [9.99936381e-01, 1.03449578e-02, 4.49613064e-03],
                [-1.03447736e-02, 9.99946489e-01, -6.42335961e-05],
                [-4.49655455e-03, 1.77180562e-05, 9.99989890e-01],
            ],
            [2.37002549e08, -2.07647061e08, -7.54694534e07],
            (-0.23491716, 140.17987182, 35792021.2420001),
            0,
            0,
        ),
        (
            50131.01736111,
            (960218, 2500),
            [16547533.6691137, -38787003.10533711, -242770.27248672],
            [2827.5914462, 1206.72876414, 10.33311542],
            [-32388646.84104986, 27004804.37195345, -165874.85452439],
            [0.78027439, 0.40162218, 22.96872279],
            153.51867545,
            (330.17317044, -12.17578748),
            (177.27392574, -11.95046228),
            [
                [9.99936381e-01, 1.03449595e-02, 4.49613140e-03],
                [-1.03447753e-02, 9.99946489e-01, -6.42326125e-05],
                [-4.49655529e-03, 1.77170571e-05, 9.99989890e-01],
            ],
            [2.36386506e08, -2.07787291e08, -7.53944111e07],
            (-0.22560065, 140.17953905, 35791892.18395986),
            0,
            0,
        ),
        (
            50131.02083333,
            (960218, 3000),
            [17391785.98229151, -38415736.18212036, -239612.68950141],
            [2800.53288309, 1268.28546791, 10.71659666],
            [-32388413.67874206, 27004922.07123395, -158945.30610131],
            [0.77457509, 0.38362576, 23.2265907],
            154.77209777,
            (330.17624281, -12.17462353),
            (176.02357057, -11.94929096),
            [
                [9.99936381e-01, 1.03449612e-02, 4.49613215e-03],
                [-1.03447770e-02, 9.99946489e-01, -6.42316291e-05],
                [-4.49655603e-03, 1.77160583e-05, 9.99989890e-01],
            ],
            [2.35778185e08, -2.07945887e08, -7.53194268e07],
            (-0.21617663, 140.17921335, 35791761.76173551),
            0,
            0,
        ),
    ],
    dtype=vissr.ORBIT_PREDICTION_DATA,
)
