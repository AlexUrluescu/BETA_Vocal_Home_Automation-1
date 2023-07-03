import React from "react";

const CircleData = ({ data, classStyle, text }) => {
  return (
    <div className={classStyle}>
      {data}
      <sup className="text-lg">{text}</sup>
    </div>
  );
};

export default CircleData;
