import { FC } from "react";

import { cn } from "@utils";
import { Card, Typography, Row, Col } from "antd";

import "./Page.scss";

const { Title, Paragraph } = Typography;

const b = cn("faq");

const Faq: FC = function () {
    return (
        <div className={b()}>
            <div className={b("inner")}>
                <div className={b("title")}>
                    <Title level={1}>FAQ</Title>
                </div>
                <div className={b("content")}>
                    <Row
                        gutter={[16, 16]}
                        style={{
                            margin: "40px 0",
                        }}
                    >
                        <Col span={12} style={{ display: "flex", flexDirection: "column" }}>
                            <Card>
                                <Title level={4}>What are IoT air quality sensors?</Title>
                                <Paragraph>
                                    IoT air quality sensors are devices that are used to monitor air pollution levels in
                                    real time. They are usually installed in various areas of the city and collect data
                                    on the content of harmful substances in the atmosphere, such as nitrogen oxides,
                                    carbon dioxide, small particles and others.
                                </Paragraph>
                                <Title level={4}>What are the benefits of air quality data visualization?</Title>
                                <Paragraph>
                                    Visualizing air quality data allows you to visually track changes in air pollution
                                    levels in different parts of a city or region. This helps residents and
                                    organizations make informed decisions about health and safety.
                                </Paragraph>
                                <Title level={4}>What air quality data do you collect?</Title>
                                <Paragraph>
                                    We collect data on the content of various harmful substances in the atmosphere, such
                                    as nitrogen dioxide (NO2), carbon oxides (CO), fine particles (PM2.5), ozone (O3)
                                    and others. This data provides valuable information about the current state of the
                                    air and its impact on health.
                                </Paragraph>
                                <Title level={4}>How often is the data on your site updated?</Title>
                                <Paragraph>
                                    We update air quality data on our website in real time. Information on the content
                                    of harmful substances is updated continuously as new data is received from our IoT
                                    sensors.
                                </Paragraph>
                            </Card>
                        </Col>
                        <Col
                            span={12}
                            style={{ display: "flex", flexDirection: "column", gap: "20px", alignItems: "center" }}
                        >
                            <img src="/assets/images/Kazakhstan.png" alt="kazakhstan" style={{ width: "100%" }} />
                            <img src="/assets/images/Zhetisu.png" alt="Zhetisu" style={{ width: "100%" }} />
                        </Col>
                    </Row>
                </div>
            </div>
        </div>
    );
};

export { Faq };
