import { FC } from "react";

import { Typography } from "antd";

import { cn } from "@utils";

import "./Page.scss";

const { Title, Text } = Typography;

const b = cn("about");

const About: FC = function () {
    return (
        <div className={b()}>
            <div className={b("inner")}>
                <div className={b("title")}>
                    <Title level={1}>Dear users</Title>
                </div>
                <div className={b("content")}>
                    <Text>
                        Our project to create a website for visualizing and analyzing air quality data is an initiative
                        to raise awareness of the importance of caring for the environment and the health of urban
                        populations.
                    </Text>
                    <Text>
                        We collect air quality data using modern IoT sensors installed in various parts of the city. Our
                        efforts are aimed at providing the public with access to this information in a convenient and
                        understandable format.
                    </Text>
                    <Text>
                        Our team is made up of experts in web development, design and data analysis who work to make our
                        site the hub for air quality information in your city.
                    </Text>
                    <Text>
                        We hope our project will help you be more aware of the environment and make more informed
                        decisions to maintain your health and well-being.
                    </Text>
                    <Text>Sincerely,</Text>
                    <Typography>Air quality data visualization project team.</Typography>
                </div>
            </div>
        </div>
    );
};

export { About };
