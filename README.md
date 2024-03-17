# EpiFund

EpiFund is a standalone Frappe application designed to manage equity distribution in startups using the dynamic "Slicing Pie" model. It provides a flexible and transparent system for tracking contributions and allocating equity to founders and early contributors. [Slicing Pie](https://slicingpie.com) is an excellent book by Mike Moyer that provides a detailed explanation of the model.

## The Slicing Pie Model

The Slicing Pie model is an innovative approach to equity distribution that ensures fairness and adaptability. It dynamically allocates equity based on the relative value of each participant's contributions, rather than fixed percentages. This model is particularly well-suited for startups in their early stages, where the value of contributions can be difficult to quantify, and the equity needs may change over time.

## Why "Founder" Instead of "Grunt"

In EpiFund, we use the term "Founder" to refer to individuals contributing to the startup, as opposed to the traditional "Grunt" used in the Slicing Pie model. We believe that "Founder" better reflects the significant role these individuals play in establishing and shaping the startup. It also aligns with the transition to a more formal company structure as the startup matures.

## Key Features

- **Founder Management:** Track founders and their contributions and equity stakes.
- **Contribution Tracking:** Record various types of contributions, including time, cash, resources, and intellectual property, and assign points based on their value.
- **Equity Calculation:** Dynamically calculate equity percentages for each Founder based on their share of the total points in the fund.
- **Founder Fund:** Create and manage separate funds, each with its own set of contributions and equity distribution.
- **Integration:** Optionally integrate with ERPNext for enhanced functionality, such as linking Founders to Employees and Shareholders, when ERPNext is available.

## DocTypes

- **Founder:** Represents an individual contributing to the startup.
- **Contribution:** Records a contribution made by a Founder.
- **Founder Position:** Defines the role or position of a Founder within the startup.
- **Contribution Type:** Specifies the type of contribution (e.g., time, cash, resources).
- **Founder Fund:** Represents a fund consisting of contributions from multiple Founders.

## Installation

To install EpiFund on your Frappe site, follow these steps:

1. Clone the EpiFund repository:
   ```bash
   git clone https://github.com/your-repo/epifund.git
   ```

2. Install the app on your site:
   ```bash
   bench --site your-site-name install-app epifund
   ```

3. Migrate your site to apply the changes:
   ```bash
   bench --site your-site-name migrate
   ```

## Usage

1. **Create Founders:** Add individuals who are contributing to the startup as Founders in EpiFund.
2. **Record Contributions:** Log contributions made by each Founder, specifying the type, value, and date of contribution.
3. **View Equity Distribution:** Check the equity percentage for each Founder based on the points accumulated from their contributions.
4. **Manage Founder Funds:** Create and manage separate funds for different projects or phases of the startup.

## Future Plans

- Integration with ERPNext's Employee and Shareholder doctypes (planned for version 0.2).
- Enhanced reporting and analytics features.
- Additional customization options for contribution types and equity calculations.

## Contributing

Contributions to EpiFund are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

## License

EpiFund is released under the [MIT License](LICENSE).

---

You can further customize this `README.md` file to reflect any additional features or changes in EpiFund.