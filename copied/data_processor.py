import random
import string

def generate_random_string(length=6):
    """Generates a random string of uppercase letters."""
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def create_nested_dictionary(num_entries=5):
    """Creates a nested dictionary with random keys and values."""
    data = {}
    for _ in range(num_entries):
        key = generate_random_string()
        data[key] = {
            'id': random.randint(1000, 9999),
            'values': [random.random() for _ in range(3)],
            'metadata': {
                'created_by': generate_random_string(3),
                'tags': [generate_random_string(2) for _ in range(2)]
            }
        }
    return data

def summarize_dictionary(data):
    """Summarizes the contents of the nested dictionary."""
    summary = {
        'total_entries': len(data),
        'average_values': [],
        'unique_tags': set()
    }

    total_values = [0.0, 0.0, 0.0]
    for entry in data.values():
        for i, val in enumerate(entry['values']):
            total_values[i] += val
        summary['unique_tags'].update(entry['metadata']['tags'])

    summary['average_values'] = [round(val / len(data), 2) for val in total_values]
    summary['unique_tags'] = list(summary['unique_tags'])
    return summary

def display_summary(summary):
    """Displays the summary in a formatted way."""
    print("📊 Dictionary Summary:")
    print(f"Total Entries: {summary['total_entries']}")
    print(f"Average Values: {summary['average_values']}")
    print(f"Unique Tags: {', '.join(summary['unique_tags'])}")

def main():
    print("🔧 Generating complex nested dictionary...")
    data = create_nested_dictionary(10)
    print("✅ Dictionary created. Now summarizing...")
    summary = summarize_dictionary(data)
    display_summary(summary)

if __name__ == "__main__":
    main()
