from app.seeders.settings_seeder import seed_settings
import click

@click.command("seed-settings")
def seed_settings_command():
    """Command to seed the settings table with the default AI system message."""
    try:
        # Call the seeder function
        seed_settings()
        print("Settings seeded successfully.")
    except Exception as e:
        print(f"Error seeding settings: {e}")
