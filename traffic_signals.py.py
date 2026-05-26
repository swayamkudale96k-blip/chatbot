import time

def traffic_light_controller():
    while True:
        print("\n--- Smart Traffic Light Controller ---")

        lane_a = int(input("Enter vehicles in Lane A: "))
        lane_b = int(input("Enter vehicles in Lane B: "))
        lane_c = int(input("Enter vehicles in Lane C: "))
        lane_d = int(input("Enter vehicles in Lane D: "))

        traffic = {
            "Lane A": lane_a,
            "Lane B": lane_b,
            "Lane C": lane_c,
            "Lane D": lane_d
        }

        # Find lane with highest traffic
        green_lane = max(traffic, key=traffic.get)

        print("\nVehicle Count:")
        for lane, count in traffic.items():
            print(f"{lane}: {count}")

        print(f"\nGREEN Signal -> {green_lane}")

        # Green time based on traffic density
        green_time = min(traffic[green_lane] * 2, 30)

        print(f"{green_lane} will stay GREEN for {green_time} seconds")
        time.sleep(3)

        choice = input("\nRun again? (y/n): ").lower()
        if choice != 'y':
            print("System Stopped.")
            break

traffic_light_controller()
