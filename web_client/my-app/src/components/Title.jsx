import React from "react";

const Title = ({ title, classStyle }) => {
  return (
    <div className="p-3 mb-20">
      <h1 className={classStyle}>{title}</h1>
    </div>
  );
};

export default Title;
