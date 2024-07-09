import matplotlib.pyplot as plt

# Function to convert time in minute.second.millisecond.microsecond format to seconds
def convert_time_to_seconds(time_str):
    minute, second, millisecond, microsecond = map(int, time_str.split('.'))
    return minute * 60 + second + millisecond / 1000 + microsecond / 1000000

# Read the data from the text file
def read_data(file_path):
    times = []
    voltages = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                time_str, voltage_str = parts
                times.append(convert_time_to_seconds(time_str))
                voltages.append(float(voltage_str))
    return times, voltages

# Plot the data
def plot_data(times, voltages):
    # Calculate the maximum second value for the x-axis limit
    max_second = int(times[-1]) + 1

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(times, voltages)

    # Set the x-axis limit and labels
    ax.set_xlim([0, max_second])
    ax.set_xticks(range(0, max_second + 1))  # Set x-axis ticks to be whole seconds
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Voltage')

    # Display the plot
    plt.show()

# Main function
def main():
    file_path = 'voltage_data.txt'  # Change this to your actual file path
    times, voltages = read_data(file_path)
    plot_data(times, voltages)

# Run the main function
if __name__ == '__main__':
    main()
